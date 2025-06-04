import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler
from telegram import Update
from itinerario import generar_itinerario
from prompts import verificar_destino, validar_fechas

from flask import Flask, request
import logging

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # URL pública de tu bot

# Estados
DESTINO, FECHAS, DIRECCION, TRANSPORTE, INTERESES, PASEOS = range(6)

app = Flask(__name__)
application = ApplicationBuilder().token(BOT_TOKEN).build()

# Handlers (igual que antes)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): ...
async def destino(update: Update, context: ContextTypes.DEFAULT_TYPE): ...
async def fechas(update: Update, context: ContextTypes.DEFAULT_TYPE): ...
async def direccion(update: Update, context: ContextTypes.DEFAULT_TYPE): ...
async def transporte(update: Update, context: ContextTypes.DEFAULT_TYPE): ...
async def intereses(update: Update, context: ContextTypes.DEFAULT_TYPE): ...
async def paseos(update: Update, context: ContextTypes.DEFAULT_TYPE): ...
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE): ...

# Conversación
conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        DESTINO: [MessageHandler(filters.TEXT & ~filters.COMMAND, destino)],
        FECHAS: [MessageHandler(filters.TEXT & ~filters.COMMAND, fechas)],
        DIRECCION: [MessageHandler(filters.TEXT & ~filters.COMMAND, direccion)],
        TRANSPORTE: [MessageHandler(filters.TEXT & ~filters.COMMAND, transporte)],
        INTERESES: [MessageHandler(filters.TEXT & ~filters.COMMAND, intereses)],
        PASEOS: [MessageHandler(filters.TEXT & ~filters.COMMAND, paseos)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)

application.add_handler(conv_handler)

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def telegram_webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put_nowait(update)
    return "ok"

@app.route("/", methods=["GET"])
def index():
    return "Bot activo"

if __name__ == "__main__":
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        webhook_url=f"{WEBHOOK_URL}/{BOT_TOKEN}",
    )
