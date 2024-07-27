from aiogram import Bot, Dispatcher, types, filters, F
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
bot = Bot(token="7293388343:AAES-oqXbnmEQObzUCo7okybobgAUUy1q0w")
dp = Dispatcher(bot=bot)

main_button = ReplyKeyboardMarkup(keyboard= [
    [KeyboardButton(text="Gamburger"), KeyboardButton(text="Lavash")],
    [KeyboardButton(text="Pepsi"), KeyboardButton(text="Cola")],
    [KeyboardButton(text="Lavash kombo"), KeyboardButton(text="Sandvich")],
    [KeyboardButton(text="Orqaga qaytish")]
], resize_keyboard=True)

yes_or_no = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Ha, olaman"), KeyboardButton(text="Yoq, olmayman")]
], resize_keyboard=True)

language = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Uzbek tili"), KeyboardButton(text="Rus tili")]
], resize_keyboard=True)

main_button_rus = ReplyKeyboardMarkup(keyboard= [
    [KeyboardButton(text="Гамбургер"), KeyboardButton(text="Лаваш")],
    [KeyboardButton(text="Пепси"), KeyboardButton(text="Кола")],
    [KeyboardButton(text="Лаваш комбо"), KeyboardButton(text="Сэндвич")],
    [KeyboardButton(text="Вернуться назад")]
], resize_keyboard=True)

yes_or_no_rus = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Да, куплю"), KeyboardButton(text="Нет, не куплю")]
], resize_keyboard=True)

@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
     await message.answer(f"EVOSga xush kelibsiz😃 {message.from_user.first_name}\nДобро пожаловать в EVOS😃 {message.from_user.first_name}", reply_markup=language)

@dp.message(F.text == "Uzbek tili")
async def uzb(message: types.Message):
    await message.answer("Siz uzbek tilini tanladingiz", reply_markup=main_button)

@dp.message(F.text == "Rus tili")
async def uz_language(message: types.Message):
    await message.answer("Вы выбрали русский язык", reply_markup=main_button_rus)

@dp.message(F.text == "Orqaga qaytish")
async def uzbek_lang(message: types.Message):
    await message.answer("Siz orqaga qaytingiz", reply_markup=language)

@dp.message(filters.Command("info"))
async def info_function(message: types.Message):
     await message.answer(f"Your first name: {message.from_user.first_name}\nYour last name: {message.from_user.last_name}\nYour id: {message.from_user.id}")

@dp.message(F.text == "Gamburger")
async def evos_function(message: types.Message):
    photo = "https://api.uznews.uz/upload/images/evos.jpg"
    await message.reply_photo(photo=photo, caption="Hamburger 30.000 so'm", reply_markup=yes_or_no)

@dp.message(F.text == "Yoq, olmayman")
async def cancel(message: types.Message):
    await message.answer("Siz olmadingiz❌", reply_markup=main_button)

@dp.message(F.text == "Ha, olaman")
async def order(message: types.Message):
    await message.answer("Siz oldingiz✅", reply_markup=main_button)

@dp.message(F.text == "Lavash")
async def evos_function(message: types.Message):
    photo = "https://media.express24.uz/r/848/1500/USkw4zygayqAjhGTgd5qZ.jpg"
    await message.reply_photo(photo=photo, caption="Lavash 40.000 so'm", reply_markup=yes_or_no)

@dp.message(F.text == "Pepsi")
async def evos_function(message: types.Message):
    photo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFRatNaKPS9aNKSawzhIYjzqq6D15twcOCWA&s"
    await message.reply_photo(photo=photo, caption="Pepsi 25.000 so'm", reply_markup=yes_or_no)

@dp.message(F.text == "Sandvich")
async def evos_function(message: types.Message):
    photo ="https://www.eatingwell.com/thmb/LQXwKPvgYghCs2LH7bwlsx0gD1Q=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/cucumber-caprese-sandwich-6343482dece14c3d876bc7bac317ecd8.jpg"
    await message.reply_photo(photo=photo, caption="Sandwich 15.000 so'm", reply_markup=yes_or_no)

@dp.message(F.text == "Cola")
async def evos_function(message: types.Message):
    photo = "https://kommers.uz/wp-content/uploads/2022/02/kommers-albom-5.jpg"
    await message.reply_photo(photo=photo, caption="Coca-Cola 25.000 so'm", reply_markup=yes_or_no)

@dp.message(F.text == "Lavash kombo")
async def evos_function(message: types.Message):
    photo = "https://media.express24.uz/r/600/600/umuc8XjgzLtco1zTK7CyH.jpg"
    await message.reply_photo(photo=photo, caption="Lavash 199.000 so'm", reply_markup=yes_or_no)



@dp.message(F.text == "Вернуться назад")
async def uzbek_lang(message: types.Message):
    await message.answer("Вы вернулись назад", reply_markup=language)

@dp.message(F.text == "Гамбургер")
async def evos_function(message: types.Message):
    photo = "https://api.uznews.uz/upload/images/evos.jpg"
    await message.reply_photo(photo=photo, caption="Гамбургер 30.000 so'm", reply_markup=yes_or_no_rus)

@dp.message(F.text == "Лаваш")
async def evos_function(message: types.Message):
    photo = "https://media.express24.uz/r/848/1500/USkw4zygayqAjhGTgd5qZ.jpg"
    await message.reply_photo(photo=photo, caption="Лаваш 40.000 so'm", reply_markup=yes_or_no_rus)

@dp.message(F.text == "Пепси")
async def evos_function(message: types.Message):
    photo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFRatNaKPS9aNKSawzhIYjzqq6D15twcOCWA&s"
    await message.reply_photo(photo=photo, caption="Пепси 25.000 so'm", reply_markup=yes_or_no_rus)

@dp.message(F.text == "Сэндвич")
async def evos_function(message: types.Message):
    photo ="https://www.eatingwell.com/thmb/LQXwKPvgYghCs2LH7bwlsx0gD1Q=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/cucumber-caprese-sandwich-6343482dece14c3d876bc7bac317ecd8.jpg"
    await message.reply_photo(photo=photo, caption="Сэндвич 15.000 so'm", reply_markup=yes_or_no_rus)

@dp.message(F.text == "Кола")
async def evos_function(message: types.Message):
    photo = "https://kommers.uz/wp-content/uploads/2022/02/kommers-albom-5.jpg"
    await message.reply_photo(photo=photo, caption="Кола 25.000 so'm", reply_markup=yes_or_no_rus)

@dp.message(F.text == "Лаваш комбо")
async def evos_function(message: types.Message):
    photo = "https://media.express24.uz/r/600/600/umuc8XjgzLtco1zTK7CyH.jpg"
    await message.reply_photo(photo=photo, caption="Лаваш комбо 199.000 so'm", reply_markup=yes_or_no_rus)

@dp.message(F.text == "Нет, не куплю")
async def cancel(message: types.Message):
    await message.answer("Вы не купили❌", reply_markup=main_button_rus)

@dp.message(F.text == "Да, куплю")
async def order(message: types.Message):
    await message.answer("Вы купили✅", reply_markup=main_button_rus)

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
