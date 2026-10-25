#!/usr/bin/env python3
"""
Cosmic Free Kicks – Telegram bot launcher
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# ──────────────────────────────────────────────
# BOT TOKEN  (replace with your own if needed)
# ──────────────────────────────────────────────
TOKEN = "8843510657:AAGzWuoFgxxMcDsr-DKhHLqA1ZX8nZpa37Y"

GAME_URL = "https://madmank79.github.io/Spacepinball/"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ /start - Welcome message with play button """
    keyboard = [
        [InlineKeyboardButton("⚽ Take Free Kicks", url=GAME_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🌌 Welcome to *Cosmic Free Kicks*!\n\n"
        "Take 3 free kicks from different distances.\n"
        "Longer range = higher points!\n\n"
        "Tap the button below to play 👇",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ /play - Launch the game """
    keyboard = [
        [InlineKeyboardButton("🚀 Start Kicking", url=GAME_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Ready for some free kicks?\n"
        "Close → Medium → Long range.\n"
        "Score as many as you can!",
        reply_markup=reply_markup
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ /help - How to play """
    await update.message.reply_text(
        "⚽ *Cosmic Free Kicks – How to Play*\n\n"
        "🎯 *You get 3 free kicks:*\n"
        "• Close range → 50 points\n"
        "• Medium range → 100 points\n"
        "• Long range → 150 points\n\n"
        "🎮 *Controls:*\n"
        "• Drag left/right (or ← → / A D) to aim\n"
        "• Hold to charge power, release to shoot\n"
        "• Space / hold on mobile also works\n\n"
        "Beat the goalkeeper and rack up points!\n"
        "High score is saved on your device.\n\n"
        "Use /play to start!",
        parse_mode="Markdown"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))
    app.add_handler(CommandHandler("help", help_cmd))

    print("⚽ Cosmic Free Kicks bot is online...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
