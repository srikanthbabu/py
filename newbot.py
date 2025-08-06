# pylint: disable=unused-argument
"""
Calculating portfolio value using fyahoo
Author: Srikanth Babu
Date: 2025-08-06
"""
from telegram import Update
from telegram import InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from pywizlight import wizlight

from yahoote import portfolio_yahoo, portfolio_image
BOT_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

MENU_TEXT = (
    "📊 *Welcome!*\n\n"
    "Here are the available commands:\n"
    "🔹 /price - Check stock prices\n"
    "🔹 /portfolio - View your portfolio\n"
    "🔹 /help - Get help information\n"
    "🔹 /news - Latest market news\n"
    "🔹 /lighton - Latest market news\n"
    "🔹 /lightoff - Latest market news\n"
    "\nPlease select an option to continue."
)


# /start handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    start handler
    """
    await update.message.reply_text(MENU_TEXT, parse_mode="Markdown")


# /price handler
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    price handler
    """
    await update.message.reply_text("This is price menu")


# /price handler
async def portfolio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    portfolio handler
    """
    print("in Protfolio")
    portfolio_text = portfolio_yahoo()
    image_buffer = portfolio_image(portfolio_text)
    print(portfolio_text)
    await update.message.reply_photo(
            photo=InputFile(image_buffer, filename="portfolio.png")
    )


async def control_wiz_plugon(ip):
    """
    Function to turn on light
    """
    plug = wizlight(ip)
    await plug.turn_on()


async def control_wiz_plugoff(ip):
    """
    Function to turn off light
    """
    plug = wizlight(ip)
    await plug.turn_off()


async def wizlighton(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Turn on handler
    """
    await control_wiz_plugon("192.168.1.7")
    await update.message.reply_text("✅ Light turned ON")


async def wizlightoff(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Turn off handler
    """
    await control_wiz_plugoff("192.168.1.7")
    await update.message.reply_text("✅ Light turned OFF")


# Main bot setup
def main():
    """
    main function
    """
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("portfolio", portfolio))
    app.add_handler(CommandHandler("lighton", wizlighton))
    app.add_handler(CommandHandler("lightoff", wizlightoff))
    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
