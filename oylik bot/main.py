import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from button import *
from state import * 
from chek import *
from config import BOT_TOKEN as token



bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()

# kanal obuna
@dp.message(chek_chanal())
async def sup(m:Message):
    kanal_link = "https://t.me/sotiladigan_kanal_1_id"

    kanal_but = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1-kanal", url=kanal_link)],
        ]
    )
    await m.answer(text="Kanallarga obuna bo'ling", reply_markup=kanal_but)
    






# Commandlar bolimi boshlanishi

@dp.message(Command('start'))
async def command_start(message: Message):
    await message.answer(text=f"Qanday maoshni hisoblaymiz {html.bold(message.from_user.full_name)}?", reply_markup=base_menu)


# Commandlar bolimi tugashi










# Bosh sahifa uchun kod

@dp.message(F.text == "Bosh sahifa")
async def asd(message: Message):
    await message.answer(text="Bosh sahifa", reply_markup=base_menu)




# Soatlab ni hisoblash ni boshi 

@dp.message(F.text == "Soatlab hisoblash")
async def soatlab_def(message: Message, state: FSMContext):
    await message.answer(text="Toifangizni tanlang:", reply_markup=toifa)
    await state.set_state(soatlab.toifa)


@dp.message(soatlab.toifa)
async def soatlab_toifa(m: Message, state:FSMContext):
    if m.text == "Oliy toifa" or "1-toifa" or "2-toifa" or "Mutaxasis" or "O'rta maxsus":
        soat_toifa = m.text
    await state.update_data(toifa=soat_toifa)
    await m.answer(text="1 haftalik dars soatingiz raqam ko'rinishida yuboring:", reply_markup=bosh)
    await state.set_state(soatlab.dars_soati)


@dp.message(soatlab.dars_soati)
async def soatlab_dars_soat(m: Message, state: FSMContext):
    if not m.text.isdigit():
        await m.answer(text="Yuborgan haftalik soatda xatolik bor. Qaytadan yuboring!", reply_markup=bosh)
    else:
        soat_dars_soati = m.text
        await state.update_data(dars_soati=soat_dars_soati)
        await m.answer(text="Sinf rahbarmisiz?", reply_markup=rahbarmisiz)
        await state.set_state(soatlab.sinf_rahbarligi)


@dp.message(soatlab.sinf_rahbarligi)
async def soatlab_sinf_rah(m: Message, state:FSMContext):
    if m.text == "Ha":
        soat_sinf_rah = m.text
        await state.update_data(sinf_rahbarligi=soat_sinf_rah)
        await m.answer(text="Sinfingizdagi o'quvchilar sonini tanlang:", reply_markup=oquvchilar_soni)
        await state.set_state(soatlab.oquvchilar_soni)
    elif m.text == "Yo'q":
        soat_sinf_rah = m.text
        await state.update_data(sinf_rahbarligi=soat_sinf_rah)
        await m.answer(text="Daftar tekshirasizmi?:", reply_markup=rahbarmisiz)
        await state.set_state(soatlab.daftar_tekshirish)


@dp.message(soatlab.oquvchilar_soni)
async def soatlab_oquvchi_soni(m: Message, state: FSMContext):
    if m.text == "1-15 nafar" or "16-20 nafar" or "21-25 nafar"or"26-30 nafar"or"30 tadan ko'p":
        yuq_oquv_soni = m.text
        await state.update_data(oquvchilar_soni=yuq_oquv_soni)
        await m.answer(text="Daftar tekshirasizmi?", reply_markup=rahbarmisiz)
        await state.set_state(soatlab.daftar_tekshirish)
    else:
        await m.answer(text="Iltimos pastdagi tugmalar orqali tanlang!", reply_markup=oquvchilar_soni)


@dp.message(soatlab.daftar_tekshirish)
async def daftar(m:Message, state:FSMContext):
    if m.text == "Ha":
        soatlab_daftar_tekshir = 1
        await state.update_data(daftar_tekshirish=soatlab_daftar_tekshir)
        await m.answer(text="Nechanchi sinflarni daftarini tekshirasiz?", reply_markup=nechanchi_sinf_daftar)
        await state.set_state(soatlab.daftar_sinfi)
    elif m.text == "Yo'q":
        soatlab_daftar_tekshir = 0
        await state.update_data(daftar_tekshirish=soatlab_daftar_tekshir)
        await m.answer(text="Kabinet mudirlik vazifasi bormi?", reply_markup=rahbarmisiz)
        await state.set_state(soatlab.kabinet)


@dp.message(soatlab.daftar_sinfi)
async def soat_daftar_sinfi(m:Message, state:FSMContext):
    if m.text == "1-4 sinflar" or "5-11 sinflar":
        soatlab_daftar_sinfi = m.text
        await state.update_data(daftar_sinfi=soatlab_daftar_sinfi)
        await m.answer(text="Haftada necha soat daftar tekshirasiz? Raqamlarda yuboring:", reply_markup=bosh)
        await state.set_state(soatlab.daftar_tekshirish_soati)
    else:
        await m.answer(text="Iltimos pastdagi tugmalar orqali tanlang!", reply_markup=nechanchi_sinf_daftar)


@dp.message(soatlab.daftar_tekshirish_soati)
async def  soatlab_daftar_soati(m: Message, state: FSMContext):
    if m.text.isdigit():
        soatlab_daftar_soat = m.text
    elif m.text == "Menga daftar tekshirganimga to'lanmaydi":
        soatlab_daftar_soat = 0
    await state.update_data(daftar_tekshirish_soati=soatlab_daftar_soat)
    await m.answer(text="Kabinet mudirlik vazifasi bormi?", reply_markup=rahbarmisiz)
    await state.set_state(soatlab.kabinet) 


@dp.message(soatlab.kabinet)
async def soatlab_kabi(m: Message, state: FSMContext):
    if m.text == "Ha":
        soatlab_kabine = 203280
    elif m.text == "Yo'q":
        soatlab_kabine = 0
    else:
        await m.answer(text="Iltimos kunlarni pastdagi tugmalar orqali tanlang!", reply_markup=rahbarmisiz)
    await state.update_data(kabinet=soatlab_kabine)
    await m.answer(text="Milliy yoki xalqaro darajadagi sertifikatingiz bormi? Sertifikat ustama foizini raqamlarda  kiriting:", reply_markup=sertifikat_bor)
    await state.set_state(soatlab.sertifikat)



@dp.message(soatlab.sertifikat)
async def soatlab_serti(m: Message, state: FSMContext):
    if m.text.isdigit():
        yuq_sertifi = m.text
    elif m.text == "Menda sertifikatlar yo'q":
        yuq_sertifi = 0
    else:
        await m.answer(text="Yuborgan foizda xatolik bor. Qaytadan yuboring!", reply_markup=sertifikat_bor)
    await state.update_data(sertifikat=yuq_sertifi)
    await m.answer(text="823-qaror bo‘yicha olingan ustamangiz bormi? Ustama foizini raqamlarda  kiriting:", reply_markup=ustama_bor)
    await state.set_state(soatlab.ustama)


@dp.message(soatlab.ustama)
async def soatlab_usta(m: Message, state:FSMContext):
    if m.text.isdigit():
        soatlab_ustam = m.text
    elif m.text == "Menda ustamalar yo'q":
        soatlab_ustam = 0
    else:
        await m.answer(text="Yuborgan foizda xatolik bor. Qaytadan yuboring!", reply_markup=ustama_bor)
    await state.update_data(ustama=soatlab_ustam)
    user_data = await state.get_data()
    soatlab_toifa = user_data.get("toifa")
    soatlab_dars_soati = user_data.get("dars_soati")
    soatlab_sinf_rahbarligi = user_data.get("sinf_rahbarligi")
    soatlab_oquvchilar_soni = user_data.get("oquvchilar_soni")
    soatlab_daftar_tekshirish = user_data.get("daftar_tekshirish")
    if soatlab_daftar_tekshirish == 1:
        soatlab_daftar_tekshirish_soati = user_data.get("daftar_tekshirish_soati")
    elif soatlab_daftar_tekshirish == 0:
        soatlab_daftar_tekshirish_soati = 0
    soatlab_kabinet = user_data.get("kabinet")
    soatlab_sertifikat = user_data.get("sertifikat")
    soatlab_ustama = user_data.get("ustama")
    if soatlab_toifa == "Oliy toifa":
        soat_maoshi =  241210
    elif soatlab_toifa == "1-toifa":
        soat_maoshi = 218276
    elif soatlab_toifa == "2-toifa":
        soat_maoshi = 195885
    elif soatlab_toifa == "Mutaxasis":
        soat_maoshi = 174967
    elif soatlab_toifa == "O'rta maxsus":
        soat_maoshi = 163553


    
    if soatlab_oquvchilar_soni == "1-15 nafar":
        oquv_soni = 304920
    elif soatlab_oquvchilar_soni == "16-20 nafar":
        oquv_soni = 364980
    elif soatlab_oquvchilar_soni == "21-25 nafar":
        oquv_soni = 426195
    elif soatlab_oquvchilar_soni == "26-30 nafar":
        oquv_soni = 486255
    elif soatlab_oquvchilar_soni == "30 tadan ko'p":
        oquv_soni = 609840
    elif soatlab_sinf_rahbarligi == "Yo'q":
        oquv_soni = 0
    
    soatlab_soat_ishlash_maoshi = soat_maoshi * int(soatlab_dars_soati)
    soatlab_daftar_tek_soati = int(soatlab_daftar_tekshirish_soati) * 9843
    soatlab_sertifika = soatlab_soat_ishlash_maoshi / 100 * int(soatlab_sertifikat)
    soatlab_ustama_foizi = soatlab_soat_ishlash_maoshi / 100 * int(soatlab_ustama)
    soatlab_nachis = soatlab_soat_ishlash_maoshi+soatlab_daftar_tek_soati+soatlab_sertifika+soatlab_ustama_foizi+oquv_soni+int(soatlab_kabinet)
    soatlab_qolga = soatlab_nachis - (soatlab_nachis / 100 * 13) 
    await m.answer(text=f"💰 Sizning jami oylik maoshingiz (Начисления): {int(soatlab_nachis):,}\n\nQo'lga tegishi: {int(soatlab_qolga):,}")
    await m.answer(text=f"Qanday maoshni hisoblaymiz {html.bold(m.from_user.full_name)}?", reply_markup=base_menu)
    await state.clear()

# Soatlab ni hisoblash ni tugashi 






# Boshlang'ich sinf ni hisoblash ni boshi 

@dp.message(F.text == "Boshlang'ich sinf")
async def boshlangi(message: Message, state: FSMContext):
    await message.answer(text="Toifangizni tanlang:", reply_markup=toifa)
    await state.set_state(boshlangich.toifa)

@dp.message(boshlangich.toifa)
async def bosh_toifa(m: Message, state:FSMContext):
    if m.text == "Oliy toifa" or "1-toifa" or "2-toifa" or "Mutaxasis" or "O'rta maxsus":
        bosh_toifa = m.text
    else:
        await m.answer(text="Iltimos pastdagi tugmalar orqali tanlang!", reply_markup=toifa)
    await state.update_data(toifa=bosh_toifa)
    await m.answer(text="1 haftalik dars soatingiz raqam ko'rinishida yuboring:", reply_markup=bosh)
    await state.set_state(boshlangich.dars_soati)


@dp.message(boshlangich.dars_soati)
async def bosh_dars_soat(m: Message, state: FSMContext):
    if not m.text.isdigit():
        await m.answer(text="Yuborgan haftalik soatda xatolik bor. Qaytadan yuboring!", reply_markup=bosh)
    else:
        bosh_dars_soati = m.text
        await state.update_data(dars_soati=bosh_dars_soati)
        await m.answer(text="Sinf rahbarmisiz?", reply_markup=rahbarmisiz)
        await state.set_state(boshlangich.sinf_rahbarligi)


@dp.message(boshlangich.sinf_rahbarligi)
async def bosh_sinf_rah(m: Message, state:FSMContext):
    if m.text == "Ha":
        sinf_rah = m.text
        await state.update_data(sinf_rahbarligi=sinf_rah)
        await m.answer(text="Sinfingizdagi o'quvchilar sonini tanlang:", reply_markup=oquvchilar_soni)
        await state.set_state(boshlangich.oquvchilar_soni)
    elif m.text == "Yo'q":
        sinf_rah = m.text
        await state.update_data(sinf_rahbarligi=sinf_rah)
        await m.answer(text="Haftada necha soat daftar tekshirasiz? Raqamlarda yuboring:", reply_markup=daftar_tek_1_4)
        await state.set_state(boshlangich.daftar_tekshirish_soati)


@dp.message(boshlangich.oquvchilar_soni)
async def oquvchi_soni(m: Message, state: FSMContext):
    if m.text == "1-15 nafar" or "16-20 nafar" or "21-25 nafar"or"26-30 nafar"or"30 tadan ko'p":
        oquv_soni = m.text
        await state.update_data(oquvchilar_soni=oquv_soni)
        await m.answer(text="Haftada necha soat daftar tekshirasiz? Raqamlarda yuboring:", reply_markup=daftar_tek_1_4)
        await state.set_state(boshlangich.daftar_tekshirish_soati)
    else:
        await m.answer(text="Iltimos pastdagi tugmalar orqali tanlang!", reply_markup=oquvchilar_soni)
        

@dp.message(boshlangich.daftar_tekshirish_soati)
async def  daftar_soati(m: Message, state: FSMContext):
    if m.text.isdigit():
        daftar_soat = m.text
    elif m.text == "Menga daftar tekshirganimga to'lanmaydi":
        daftar_soat = 0
    await state.update_data(daftar_tekshirish_soati=daftar_soat)
    await m.answer(text="Kabinet mudirlik vazifasi bormi?", reply_markup=rahbarmisiz)
    await state.set_state(boshlangich.kabinet) 


@dp.message(boshlangich.kabinet)
async def kabi(m: Message, state: FSMContext):
    if m.text == "Ha":
        kabine = 203280
    elif m.text == "Yo'q":
        kabine = 0
    else:
        await m.answer(text="Iltimos kunlarni pastdagi tugmalar orqali tanlang!", reply_markup=rahbarmisiz)
    await state.update_data(kabinet=kabine)
    await m.answer(text="Milliy yoki xalqaro darajadagi sertifikatingiz bormi? Sertifikat ustama foizini raqamlarda  kiriting:", reply_markup=sertifikat_bor)
    await state.set_state(boshlangich.sertifikat)



@dp.message(boshlangich.sertifikat)
async def serti(m: Message, state: FSMContext):
    if m.text.isdigit():
        sertifi = m.text
    elif m.text == "Menda sertifikatlar yo'q":
        sertifi = 0
    else:
        await m.answer(text="Yuborgan foizda xatolik bor. Qaytadan yuboring!", reply_markup=sertifikat_bor)
    await state.update_data(sertifikat=sertifi)
    await m.answer(text="823-qaror bo‘yicha olingan ustamangiz bormi? Ustama foizini raqamlarda  kiriting:", reply_markup=ustama_bor)
    await state.set_state(boshlangich.ustama)


@dp.message(boshlangich.ustama)
async def usta(m: Message, state:FSMContext):
    if m.text.isdigit():
        ustam = m.text
    elif m.text == "Menda ustamalar yo'q":
        ustam = 0
    else:
        await m.answer(text="Yuborgan foizda xatolik bor. Qaytadan yuboring!", reply_markup=ustama_bor)
    await state.update_data(ustama=ustam)
    user_data = await state.get_data()
    toifa = user_data.get("toifa")
    dars_soati = user_data.get("dars_soati")
    sinf_rahbarligi = user_data.get("sinf_rahbarligi")
    oquvchilar_soni = user_data.get("oquvchilar_soni")
    daftar_tekshirish_soati = user_data.get("daftar_tekshirish_soati")
    kabinet = user_data.get("kabinet")
    sertifikat = user_data.get("sertifikat")
    ustama = user_data.get("ustama")
    if toifa == "Oliy toifa":
        soat_maoshi = 241210
    elif toifa == "1-toifa":
        soat_maoshi = 218276
    elif toifa == "2-toifa":
        soat_maoshi = 195885
    elif toifa == "Mutaxasis":
        soat_maoshi = 174967
    elif toifa == "O'rta maxsus":
        soat_maoshi = 163553

    
    if oquvchilar_soni == "1-15 nafar":
        oquv_soni = 304920
    elif oquvchilar_soni == "16-20 nafar":
        oquv_soni = 364980
    elif oquvchilar_soni == "21-25 nafar":
        oquv_soni = 426195
    elif oquvchilar_soni == "26-30 nafar":
        oquv_soni = 486255
    elif oquvchilar_soni == "30 tadan ko'p":
        oquv_soni = 609840
    elif sinf_rahbarligi == "Yo'q":
        oquv_soni = 0

    soat_ishlash_maoshi = soat_maoshi * int(dars_soati)
    daftar_tek_soati = int(daftar_tekshirish_soati) * 10164
    sertifika = soat_ishlash_maoshi / 100 * int(sertifikat)
    ustama_foizi = soat_ishlash_maoshi / 100 * int(ustama)
    nachis = soat_ishlash_maoshi+daftar_tek_soati+sertifika+ustama_foizi+oquv_soni+int(kabinet)
    qolga = nachis - (nachis / 100 * 13) 
    await m.answer(text=f"💰 Sizning jami oylik maoshingiz (Начисления): {int(nachis):,}\n\nQo'lga tegishi: {int(qolga):,}")
    await m.answer(text=f"Qanday maoshni hisoblaymiz {html.bold(m.from_user.full_name)}?", reply_markup=base_menu)
    await state.clear()
    



# Boshlang'ich sinf ni hisoblash ni tugashi 







# Yuqori sinf ni hisoblash ni boshi 

@dp.message(F.text == "Yuqori sinf")
async def asd(message: Message, state: FSMContext):
    await message.answer(text="Toifangizni tanlang:", reply_markup=toifa)
    await state.set_state(yuqori.toifa)



@dp.message(yuqori.toifa)
async def yuqori_toifa(m: Message, state:FSMContext):
    if m.text == "Oliy toifa" or "1-toifa" or "2-toifa" or "Mutaxasis" or "O'rta maxsus":
        yuq_toifa = m.text
    await state.update_data(toifa=yuq_toifa)
    await m.answer(text="1 haftalik dars soatingiz raqam ko'rinishida yuboring:", reply_markup=bosh)
    await state.set_state(yuqori.dars_soati)


@dp.message(yuqori.dars_soati)
async def yuq_dars_soat(m: Message, state: FSMContext):
    if not m.text.isdigit():
        await m.answer(text="Yuborgan haftalik soatda xatolik bor. Qaytadan yuboring!", reply_markup=bosh)
    else:
        yuq_dars_soati = m.text
        await state.update_data(dars_soati=yuq_dars_soati)
        await m.answer(text="Sinf rahbarmisiz?", reply_markup=rahbarmisiz)
        await state.set_state(yuqori.sinf_rahbarligi)


@dp.message(yuqori.sinf_rahbarligi)
async def bosh_sinf_rah(m: Message, state:FSMContext):
    if m.text == "Ha":
        yuq_sinf_rah = m.text
        await state.update_data(sinf_rahbarligi=yuq_sinf_rah)
        await m.answer(text="Sinfingizdagi o'quvchilar sonini tanlang:", reply_markup=oquvchilar_soni)
        await state.set_state(yuqori.oquvchilar_soni)
    elif m.text == "Yo'q":
        yuq_sinf_rah = m.text
        await state.update_data(sinf_rahbarligi=yuq_sinf_rah)
        await m.answer(text="Haftada necha soat daftar tekshirasiz? Raqamlarda yuboring:", reply_markup=daftar_tek_1_4)
        await state.set_state(yuqori.daftar_tekshirish_soati)


@dp.message(yuqori.oquvchilar_soni)
async def oquvchi_soni(m: Message, state: FSMContext):
    if m.text == "1-15 nafar" or "16-20 nafar" or "21-25 nafar"or"26-30 nafar"or"30 tadan ko'p":
        yuq_oquv_soni = m.text
        await state.update_data(oquvchilar_soni=yuq_oquv_soni)
        await m.answer(text="Haftada necha soat daftar tekshirasiz? Raqamlarda yuboring:", reply_markup=daftar_tek_1_4)
        await state.set_state(yuqori.daftar_tekshirish_soati)
    else:
        await m.answer(text="Iltimos pastdagi tugmalar orqali tanlang!", reply_markup=oquvchilar_soni)
        

@dp.message(yuqori.daftar_tekshirish_soati)
async def  daftar_soati(m: Message, state: FSMContext):
    if m.text.isdigit():
        yuq_daftar_soat = m.text
    elif m.text == "Menga daftar tekshirganimga to'lanmaydi":
        yuq_daftar_soat = 0
    await state.update_data(daftar_tekshirish_soati=yuq_daftar_soat)
    await m.answer(text="Kabinet mudirlik vazifasi bormi?", reply_markup=rahbarmisiz)
    await state.set_state(yuqori.kabinet) 


@dp.message(yuqori.kabinet)
async def kabi(m: Message, state: FSMContext):
    if m.text == "Ha":
        yuq_kabine = 203280
    elif m.text == "Yo'q":
        yuq_kabine = 0
    else:
        await m.answer(text="Iltimos kunlarni pastdagi tugmalar orqali tanlang!", reply_markup=rahbarmisiz)
    await state.update_data(kabinet=yuq_kabine)
    await m.answer(text="Milliy yoki xalqaro darajadagi sertifikatingiz bormi? Sertifikat ustama foizini raqamlarda  kiriting:", reply_markup=sertifikat_bor)
    await state.set_state(yuqori.sertifikat)



@dp.message(yuqori.sertifikat)
async def serti(m: Message, state: FSMContext):
    if m.text.isdigit():
        yuq_sertifi = m.text
    elif m.text == "Menda sertifikatlar yo'q":
        yuq_sertifi = 0
    else:
        await m.answer(text="Yuborgan foizda xatolik bor. Qaytadan yuboring!", reply_markup=sertifikat_bor)
    await state.update_data(sertifikat=yuq_sertifi)
    await m.answer(text="823-qaror bo‘yicha olingan ustamangiz bormi? Ustama foizini raqamlarda  kiriting:", reply_markup=ustama_bor)
    await state.set_state(yuqori.ustama)


@dp.message(yuqori.ustama)
async def usta(m: Message, state:FSMContext):
    if m.text.isdigit():
        yuq_ustam = m.text
    elif m.text == "Menda ustamalar yo'q":
        yuq_ustam = 0
    else:
        await m.answer(text="Yuborgan foizda xatolik bor. Qaytadan yuboring!", reply_markup=ustama_bor)
    await state.update_data(ustama=yuq_ustam)
    user_data = await state.get_data()
    yuq_toifa = user_data.get("toifa")
    yuq_dars_soati = user_data.get("dars_soati")
    yuq_sinf_rahbarligi = user_data.get("sinf_rahbarligi")
    yuq_oquvchilar_soni = user_data.get("oquvchilar_soni")
    yuq_daftar_tekshirish_soati = user_data.get("daftar_tekshirish_soati")
    yuq_kabinet = user_data.get("kabinet")
    yuq_sertifikat = user_data.get("sertifikat")
    yuq_ustama = user_data.get("ustama")
    if yuq_toifa == "Oliy toifa":
        soat_maoshi = 241210
    elif yuq_toifa == "1-toifa":
        soat_maoshi = 218276
    elif yuq_toifa == "2-toifa":
        soat_maoshi = 195885
    elif yuq_toifa == "Mutaxasis":
        soat_maoshi = 174967
    elif yuq_toifa == "O'rta maxsus":
        soat_maoshi = 163553

    
    if yuq_oquvchilar_soni == "1-15 nafar":
        oquv_soni = 304920
    elif yuq_oquvchilar_soni == "16-20 nafar":
        oquv_soni = 364980
    elif yuq_oquvchilar_soni == "21-25 nafar":
        oquv_soni = 426195
    elif yuq_oquvchilar_soni == "26-30 nafar":
        oquv_soni = 486255
    elif yuq_oquvchilar_soni == "30 tadan ko'p":
        oquv_soni = 609840
    elif yuq_sinf_rahbarligi == "Yo'q":
        oquv_soni = 0

    yuq_soat_ishlash_maoshi = soat_maoshi * int(yuq_dars_soati)
    yuq_daftar_tek_soati = int(yuq_daftar_tekshirish_soati) * 10164
    yuq_sertifika = yuq_soat_ishlash_maoshi / 100 * int(yuq_sertifikat)
    yuq_ustama_foizi = yuq_soat_ishlash_maoshi / 100 * int(yuq_ustama)
    yuq_nachis = yuq_soat_ishlash_maoshi+yuq_daftar_tek_soati+yuq_sertifika+yuq_ustama_foizi+oquv_soni+int(yuq_kabinet)
    yuq_qolga = yuq_nachis - (yuq_nachis / 100 * 13) 
    await m.answer(text=f"💰 Sizning jami oylik maoshingiz (Начисления): {int(yuq_nachis):,}\n\nQo'lga tegishi: {int(yuq_qolga):,}")
    await m.answer(text=f"Qanday maoshni hisoblaymiz {html.bold(m.from_user.full_name)}?", reply_markup=base_menu)
    await state.clear()
    

# Yuqori sinf ni hisoblash ni tugashi 









# Dekrat puli ni hisoblash ni boshi 

@dp.message(F.text == "Dekrat puli")
async def asd(message: Message, state: FSMContext):
    await state.set_state(dekrat.pul)
    await message.answer(text="Umumiy o'rtacha oyligingizni jo'nating (Начисления):", reply_markup=bosh)


@dp.message(dekrat.pul)
async def dekret_pulini_hisoblash(message: Message, state: FSMContext):
    if message.text.isdigit():
        dekrat_puli = message.text
    else:
        await message.answer(text="Yuborgan haftalik soatda xatolik bor. Qaytadan yuboring!", reply_markup=bosh)
    await state.update_data(pul=dekrat_puli)
    user_data = await state.get_data()
    pul = user_data.get("pul")
    await message.answer(text=f"💰 Sizning jami dekret pulingiz: {int(pul) * 4:,} so'm")
    await message.answer(text=f"Qanday maoshni hisoblaymiz {html.bold(message.from_user.full_name)}?", reply_markup=base_menu)
    await state.clear()

# Dekrat puli ni hisoblash ni tugashi 








# Menhat ta'tili (otpusknoy) ni hisoblash ni boshi 

@dp.message(F.text == "Menhat ta'tili (otpusknoy)")
async def tatil_puli(message: Message, state: FSMContext):
    await message.answer(text="Necha kunlik mehnat ta'tili?", reply_markup=mehnet_kuni)
    await state.set_state(tatil.kuni)

@dp.message(tatil.kuni)
async def tatil_kuni(message: Message, state: FSMContext):
    if message.text == "48 kun" or "36 kun" or "24 kun":
        tatilkuni = message.text
    else:
        await message.answer(text="Iltimos kunlarni pastdagi tugmalar orqali tanlang!", reply_markup=mehnet_kuni)
    await state.update_data(kuni=tatilkuni)
    await message.answer(text="Umumiy o'rtacha (oxirgi 9 oylik) oyligingizni jo'nating (Начисления):", reply_markup=bosh)
    await state.set_state(tatil.oylik)





@dp.message(tatil.oylik)
async def tatil_oylik(message: Message, state: FSMContext):
    if message.text.isdigit():
        tatiloylik = message.text
    else:
        await message.answer(text="Yuborgan summada xatolik bor. Qaytadan yuboring!", reply_markup=bosh)
    await state.update_data(oylik=tatiloylik)
    user_data = await state.get_data()
    kuni = user_data.get("kuni")
    oylik = user_data.get("oylik")
    a = (int(oylik) / 25.3) * int(kuni[:2])
    b = a-(a / 100 * 13.1)
    await message.answer(text=f"💰 Sizning jami mehnat ta'tili pulingiz (Начисления): {int(a):,} \n\nQo'lga tegishi: {int(b):,}")
    await message.answer(text=f"Qanday maoshni hisoblaymiz {html.bold(message.from_user.full_name)}?", reply_markup=base_menu)
    await state.clear()
    


# Menhat ta'tili (otpusknoy) ni hisoblash ni tugashi 







async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())