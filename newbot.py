from telegram import Update
from telegram import InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio
from pywizlight import wizlight


from yahoote import portfolio_yahoo, portfolio_image
BOT_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

menu_text = (
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
    await update.message.reply_text(menu_text, parse_mode="Markdown")


# /price handler
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is price menu")

# /price handler
async def portfolio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("in Protfolio")
    portfolio_text = portfolio_yahoo()
    image_buffer = portfolio_image(portfolio_text)
    print(portfolio_text)
    await update.message.reply_photo(photo=InputFile(image_buffer, filename="portfolio.png"))

async def control_wiz_plugon(ip):
    plug = wizlight(ip)
    await plug.turn_on()

async def control_wiz_plugoff(ip):
    plug = wizlight(ip)
    await plug.turn_off()

async def wizlighton(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await control_wiz_plugon("192.168.1.7")
    await update.message.reply_text("✅ Light turned ON")

async def wizlightoff(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await control_wiz_plugoff("192.168.1.7")
    await update.message.reply_text("✅ Light turned OFF")


# Main bot setup
def main():
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
