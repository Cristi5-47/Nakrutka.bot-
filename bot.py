from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8714876509:AAFPAJfpZesp_KJfKoLkf8csTYVC2CG-7TI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("SMM botga xush kelibsiz 🚀")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot ishladi...")
    app.run_polling()

if __name__ == "__main__":
    main()
