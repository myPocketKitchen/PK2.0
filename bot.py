from dotenv import load_dotenv
import os
from aiogram import types
from pk import process_image
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, InlineQueryHandler

load_dotenv()

auth_token = os.getenv("AUTH_TOKEN")
AUTH_ID = os.getenv("AUTH_ID")

# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("/start command received")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm the PK2.0 Bot, please use a command to start.")

async def ingredients(update: Update, context: ContextTypes.DEFAULT_TYPE):
    messsage = update.effective_message  # Extracts the message from the update
    print("/ingredients command received")
    if str(message.from_user.id) == AUTH_ID:
        # Authorized user; perform the action
        # await context.bot.send_message(chat_id=update.effective_chat.id, text="You are authorized to perform this action.")

        # Run OPENAI API Call
        print("User is authorized, running API call")
        global ingredients_list
        ingredients_list = process_image(path)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=ingredients_list)

    else:
        # Request password for unauthorized users
        await context.bot.send_message(chat_id=update.effective_chat.id, text="You are not authorized to perform this action.")

async def recipe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("/recipe command received")
    if str(message.from_user.id) == AUTHORIZED_USER_ID:
        # Authorized user; perform the action
        await message.reply("You are authorized to perform this action.")

        # Run OPENAI API Call
        global ingredients_list
        recipe = get_recipes(ingredients_list)
        await message.reply(recipe)


if __name__ == '__main__':
    print("Starting bot...")
    application = ApplicationBuilder().token(auth_token).build()
    
    start_handler = CommandHandler('start', start)
    ingredients_handler = CommandHandler('ingredients', ingredients)
    recipe_handler = CommandHandler('recipe', recipe)

    application.add_handler(start_handler)
    application.add_handler(ingredients_handler)
    application.add_handler(recipe_handler)

    application.run_polling()

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––