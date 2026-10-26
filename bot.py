#!/usr/bin/env python3
"""
Cosmic Free Kicks – Telegram bot launcher
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# ──────────────────────────────────────────────
# BOT TOKEN
# ──────────────────────────────────────────────
TOKEN = "8843510657:AAGzWuoFgxxMcDsr-DKhHLqA1ZX8nZpa37Y"

# Updated to your new FreeKicks GitHub Pages URL
GAME_URL = "https://madmank79.github.io/FreeKicks/"

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
        "Score free kicks until you miss!\n"
        "Every goal increases the difficulty.\n\n"
        "How long can you keep the streak going?\n\n"
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
        "Ready for endless free kicks?\n"
        "Keep scoring to build your streak!\n"
        "One miss and it's game over.",
        reply_markup=reply_markup
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ /help - How to play """
    await update.message.reply_text(
        "⚽ *Cosmic Free Kicks – How to Play*\n\n"
        "🎯 *Endless mode:*\n"
        "Keep scoring free kicks until you miss!\n"
        "Every goal adds points and increases difficulty.\n\n"
        "• More defenders appear\n"
        "• Longer distances\n"
        "• Faster moving wall\n\n"
        "🎮 *Controls:*\n"
        "• Drag left/right (or ← → / A D) to aim\n"
        "• Hold to charge power, release to shoot\n"
        "• Space / hold on mobile also works\n\n"
        "How long can you keep the streak going?\n"
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
