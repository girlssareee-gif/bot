import os
import sqlite3
import qrcode
import random
import string
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = "PUT_YOUR_NEW_TOKEN"
ADMIN_ID = 7705209352
UPI_ID = "niteshextema@fam"

# ===== DATABASE =====
conn = sqlite3.connect("bot.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    balance INTEGER DEFAULT 0,
    promo_used INTEGER DEFAULT 0
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id TEXT,
    user_id INTEGER,
    amount INTEGER,
    status TEXT
)
""")

conn.commit()

PROMO = {"NEW10": 10}


# ===== ORDER ID =====
def generate_order_id():
    prefix = "ORD"
    rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{prefix}-{rand}"


# ===== USER =====
def get_user(user_id):
    cur.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = cur.fetchone()

    if not user:
        cur.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
        conn.commit()
        return {"balance": 0, "promo_used": 0}

    return {"balance": user[1], "promo_used": user[2]}


def update_balance(user_id, amount):
    cur.execute("UPDATE users SET balance = balance + ? WHERE user_id=?", (amount, user_id))
    conn.commit()


# ===== QR PREMIUM =====
def generate_qr(amount, user_id):
    name = "PRO BOT"
    note = f"Order {user_id}"

    link = f"upi://pay?pa={UPI_ID}&pn={name}&am={amount}&cu=INR&tn={note}"

    file = f"qr_{user_id}_{amount}.png"
    img = qrcode.make(link)
    img.save(file)
    return file


# ===== START =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💰 Wallet", callback_data="wallet")],
        [InlineKeyboardButton("📦 Order", callback_data="order")],
        [InlineKeyboardButton("🎯 Promo", callback_data="promo")],
        [InlineKeyboardButton("🛠 Support", callback_data="support")]
    ]
    await update.message.reply_text("🔥 PRO BOT READY", reply_markup=InlineKeyboardMarkup(keyboard))


# ===== BUTTON =====
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if query.data == "wallet":
        user = get_user(user_id)
        await query.message.reply_text(f"💰 Balance: ₹{user['balance']}")

    elif query.data == "order":
        keyboard = [
            [InlineKeyboardButton("1K Followers - ₹20", callback_data="buy_20")],
            [InlineKeyboardButton("2K Followers - ₹40", callback_data="buy_40")],
            [InlineKeyboardButton("5K Followers - ₹100", callback_data="buy_100")],
            [InlineKeyboardButton("10K Followers - ₹200", callback_data="buy_200")],
            [InlineKeyboardButton("50K Followers - ₹500", callback_data="buy_500")]
        ]
        await query.message.reply_text("📦 Choose Plan", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data.startswith("buy_"):
        amt = int(query.data.split("_")[1])
        context.user_data["amount"] = amt
        context.user_data["step"] = "username"
        await query.message.reply_text("📌 Send username")

    elif query.data == "promo":
        context.user_data["step"] = "promo"
        await query.message.reply_text("Send promo code")

    elif query.data == "support":
        context.user_data["step"] = "support"
        await query.message.reply_text("🛠 Send your message")


# ===== MESSAGE =====
async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text
    user = get_user(user_id)

    # USERNAME STEP
    if context.user_data.get("step") == "username":
        amt = context.user_data["amount"]
        order_id = generate_order_id()

        cur.execute("INSERT INTO orders (order_id, user_id, amount, status) VALUES (?, ?, ?, ?)",
                    (order_id, user_id, amt, "pending"))
        conn.commit()

        context.user_data["order_id"] = order_id

        qr = generate_qr(amt, user_id)
        with open(qr, "rb") as f:
            await update.message.reply_photo(
                photo=f,
                caption=f"🧾 Order ID: {order_id}\n💰 Pay ₹{amt}\n📸 Send screenshot"
            )
        os.remove(qr)

        context.user_data["step"] = "payment"

    # PROMO
    elif context.user_data.get("step") == "promo":
        if user["promo_used"]:
            await update.message.reply_text("❌ Promo already used")
            return

        code = text.upper()
        if code in PROMO:
            update_balance(user_id, PROMO[code])
            cur.execute("UPDATE users SET promo_used=1 WHERE user_id=?", (user_id,))
            conn.commit()
            await update.message.reply_text("✅ Promo applied")
        else:
            await update.message.reply_text("❌ Invalid code")

        context.user_data["step"] = None

    # SUPPORT
    elif context.user_data.get("step") == "support":
        keyboard = [[InlineKeyboardButton("Reply", callback_data=f"reply_{user_id}")]]
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"📩 SUPPORT\n🧾 Order: {context.user_data.get('order_id')}\n👤 User: {user_id}\n💬 {text}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        await update.message.reply_text("✅ Sent to support")
        context.user_data["step"] = None

    # ADMIN REPLY
    elif context.user_data.get("reply_to"):
        uid = context.user_data["reply_to"]
        await context.bot.send_message(uid, f"🛠 Support Reply:\n\n{text}")
        await update.message.reply_text("✅ Reply sent")
        context.user_data["reply_to"] = None


# ===== PHOTO =====
async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    file = await update.message.photo[-1].get_file()

    path = f"{user.id}.jpg"
    await file.download_to_drive(path)

    order_id = context.user_data.get("order_id")

    keyboard = [
        [
            InlineKeyboardButton("✅ Approve", callback_data=f"ok_{user.id}"),
            InlineKeyboardButton("❌ Reject", callback_data=f"no_{user.id}")
        ]
    ]

    with open(path, "rb") as f:
        await context.bot.send_photo(
            chat_id=ADMIN_ID,
            photo=f,
            caption=f"🧾 Order ID: {order_id}\n👤 User: {user.id}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    os.remove(path)


# ===== ADMIN =====
async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data.startswith("ok_") or data.startswith("no_"):
        action, uid = data.split("_")
        uid = int(uid)

        if action == "ok":
            cur.execute("SELECT order_id, amount FROM orders WHERE user_id=? AND status='pending' LIMIT 1", (uid,))
            order = cur.fetchone()

            if order:
                oid, amt = order
                update_balance(uid, amt)

                cur.execute("UPDATE orders SET status='done' WHERE order_id=?", (oid,))
                conn.commit()

                await context.bot.send_message(uid, f"✅ Payment Approved\n🧾 {oid}\n💰 ₹{amt}")
        else:
            await context.bot.send_message(uid, "❌ Payment Rejected")

    elif data.startswith("reply_"):
        uid = int(data.split("_")[1])
        context.user_data["reply_to"] = uid
        await query.message.reply_text("✍️ Send reply message")


# ===== MAIN =====
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CallbackQueryHandler(admin, pattern="^(ok|no|reply)_"))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))
    app.add_handler(MessageHandler(filters.PHOTO, photo))

    print("🔥 ULTIMATE BOT RUNNING...")
    app.run_polling()


if __name__ == "__main__":
    main()
