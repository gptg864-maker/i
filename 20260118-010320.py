import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8476109054:AAHirj7mlidgj2WQLqAp4iZD1ZT2ZUfuN_4"

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="♻️ Перезапуск бота")],
        [KeyboardButton(text="💰 Поповнення коштів")],
        [KeyboardButton(text="💸 Вивід коштів")],
        [KeyboardButton(text="👨‍💼 Оператор клубу")],
        [KeyboardButton(text="🎁 Бонуси")],
        [KeyboardButton(text="📢 Канал клубу")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        "♠️ Hard River Poker Club\n\nВиберіть дію 👇",
        reply_markup=menu
    )

@dp.message(Command("deposit"))
async def deposit_cmd(message: types.Message):
    await message.answer("💰 Поповнення коштів\nЗверніться до оператора: @Patriot0297")

@dp.message(Command("payout"))
async def payout_cmd(message: types.Message):
    await message.answer("💸 Вивід коштів\nНапишіть оператору: @Patriot0297")

@dp.message(Command("operator"))
async def operator_cmd(message: types.Message):
    await message.answer("👨‍💼 Оператор клубу\n@Patriot0297")

@dp.message(Command("bonus"))
async def bonus_cmd(message: types.Message):
    await message.answer("🎁 Бонуси\nФриролли, бонуси за депозит, акції")

@dp.message(Command("channel"))
async def channel_cmd(message: types.Message):
    await message.answer("📢 Канал клубу:\nhttps://t.me/your_channel")

# Кнопки
@dp.message(lambda m: m.text == "♻️ Перезапуск бота")
async def restart_btn(message: types.Message):
    await start_cmd(message)

@dp.message(lambda m: m.text == "💰 Поповнення коштів")
async def deposit_btn(message: types.Message):
    await deposit_cmd(message)

@dp.message(lambda m: m.text == "💸 Вивід коштів")
async def payout_btn(message: types.Message):
    await payout_cmd(message)

@dp.message(lambda m: m.text == "👨‍💼 Оператор клубу")
async def operator_btn(message: types.Message):
    await operator_cmd(message)

@dp.message(lambda m: m.text == "🎁 Бонуси")
async def bonus_btn(message: types.Message):
    await bonus_cmd(message)

@dp.message(lambda m: m.text == "📢 Канал клубу")
async def channel_btn(message: types.Message):
    await channel_cmd(message)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())