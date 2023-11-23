import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين سي ار","المطورين","مطورين","مطورين cr"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e7bb54b34faadd2c9b199.jpg",
        caption=f"""**⩹━★⊷━⌞  𝑪𝑹 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين cr ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞  𝑪𝑹 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒•𝑬3𝒅𝑨𝒎• اعـــــــــدامَّّ ", url=f"https://t.me/DAD_E3DAM"), 
                 ],[
                    InlineKeyboardButton(
                        "𓆩𝗠𝗔𝗡𝗗𝗢𝗢𖠲𓆪", url=f"https://t.me/M_S_2A"),
                ],[
                    InlineKeyboardButton(
                        "༤ 𝗧𝗜𝗟𝗔𝗡𝗢༒ 𝗞𝗘𝗘𝗣𝗘𝗥 ༒ 𝗜𝗦𝗠𝗔𝗟𝗜𝗔", url=f"https://t.me/TT_TXI"),
                    InlineKeyboardButton(
                        "𝐄3𝐃𝐀𝐌", url=f"https://t.me/DAD_E3DAM"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞  𝑪𝑹 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡", url=f"https://t.me/SOURCE_CR"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["كريم","منذر","منزر","كيمو","monzer","باشا"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("DAD_E3DAM")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞  𝑪𝑹 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞  𝑪𝑹 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["اعدام","اعدومتي","اعدام","عدام باشا","Adam","اخو منذر"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("devpokemon")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞  𝑪𝑹 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞  𝑪𝑹 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["تيلانو","طلايانو","شق منذر","العلق","تيلانو","تيلانو"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("dr_criss")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞  𝑪𝑹 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞  𝑪𝑹 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    

@app.on_message(
    command(["ماندو","مانو","الممول","mano","Mano"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("M_S_2A")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞  𝑪𝑹 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞  𝑪𝑹 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["/api"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/520cb8756d31bb3184de2.jpg",
        caption=f"""**⩹⊷━⌞  𝑪𝑹 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس cr\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞  𝑪𝑹 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒•𝑬3𝒅𝑨𝒎• اعـــــــــدامَّّ", url=f"https://t.me/DAD_E3DAM"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞  𝑪𝑹 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡", url=f"https://t.me/SOURCE_CR"),
                ],

            ]

        ),

    )



@app.on_message(
    command(["قرأن"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e7bb54b34faadd2c9b199.jpg",
        caption=f"""**⩹⊷━⌞  𝑪𝑹 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس cr\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**⩹━━⌞  𝑪𝑹 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒•𝑬3𝒅𝑨𝒎• اعـــــــــدامَّّ", url=f"https://t.me/DAD_E3DAM"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞  𝑪𝑹 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡", url=f"https://t.me/SOURCE_CR"),
                ],

            ]

        ),

    )



    
