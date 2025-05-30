import logging
from telegram.ext import ApplicationBuilder, CommandHandler
import os

# Mensaje de log si algo falla
logging.basicConfig(level=logging.INFO)

# Comando /start
async def start(update, context):
    await update.message.reply_text("¡Hola! Soy tu bot y estoy funcionando 24/7 🎉")

if __name__ == '__main__':
    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN:
        raise ValueError("Falta el token de Telegram (BOT_TOKEN)")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot en funcionamiento...")
    app.run_polling()
