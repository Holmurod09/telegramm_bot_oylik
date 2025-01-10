from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup



base_menu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Soatlab hisoblash")],
        [KeyboardButton(text="Boshlang'ich sinf"), KeyboardButton(text="Yuqori sinf")],
        [KeyboardButton(text="Dekrat puli")],
        [KeyboardButton(text="Menhat ta'tili (otpusknoy)")],
        [KeyboardButton(text="Boshqa lavozimlar")]
    ],
    resize_keyboard=True
)

toifa=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Oliy toifa")],
        [KeyboardButton(text="1-toifa"), KeyboardButton(text="2-toifa")],
        [KeyboardButton(text="Mutaxasis"), KeyboardButton(text="O'rta maxsus")],
        [KeyboardButton(text="Bosh sahifa")],
    ],
    resize_keyboard=True
)


rahbarmisiz=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ha"), KeyboardButton(text="Yo'q")],
        [KeyboardButton(text="Bosh sahifa")],
    ],
    resize_keyboard=True
)

daftar_tek_1_4= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Menga daftar tekshirganimga to'lanmaydi")],
        [KeyboardButton(text="Bosh sahifa")],
    ],
    resize_keyboard=True
)


oquvchilar_soni=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1-15 nafar"), KeyboardButton(text="16-20 nafar")],
        [KeyboardButton(text="21-25 nafar"), KeyboardButton(text="26-30 nafar")],
        [KeyboardButton(text="30 tadan ko'p")],
        [KeyboardButton(text="Bosh sahifa")],
    ],
    resize_keyboard=True
)


nechanchi_sinf_daftar=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1-4 sinflar"), KeyboardButton(text="5-11 sinflar")],
        [KeyboardButton(text="Bosh sahifa")],
    ],
    resize_keyboard=True
)


sertifikat_bor=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Menda sertifikatlar yo'q")],
        [KeyboardButton(text="Bosh sahifa")],
    ],
    resize_keyboard=True
)

ustama_bor=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Menda ustamalar yo'q")],
        [KeyboardButton(text="Bosh sahifa")],
    ],
    resize_keyboard=True
)


mehnet_kuni = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="48 kun")],
        [KeyboardButton(text="36 kun")],
        [KeyboardButton(text="24 kun")],
        [KeyboardButton(text="Bosh sahifa")],
    ],
    resize_keyboard=True
)

lavozimlar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Maktab direktori")],
        [KeyboardButton(text="Direktor o'rinbosarlari: (MMIBDO', O'TIBDO')")],
        [KeyboardButton(text="Direktorning xo'jalik ishlari bo'yicha o'rinbosari")],
        [KeyboardButton(text="CHQBT rahbari")],
        [KeyboardButton(text="Psixologlar")],
        [KeyboardButton(text="Maktab laboranti")],
        [KeyboardButton(text="Kadrlar bo'yicha menejer (sekretar)")],
        [KeyboardButton(text="Kutubxona mudiri")],
        [KeyboardButton(text="Kutubxonachi")],
    ],
    resize_keyboard=True
)

direktor = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="400 o'quvchigacha")],
        [KeyboardButton(text="401-880 o'quvchigacha")],
        [KeyboardButton(text="881-1600 o'quvchigacha")],
        [KeyboardButton(text="1600dan ortiq")],
        [KeyboardButton(text="Bosh sahifa")],
    ],
    resize_keyboard=True
)

chqbt = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Oliy toifa")],
        [KeyboardButton(text="1-toifa"), KeyboardButton(text="2-toifa")],
        [KeyboardButton(text="Mutaxasis")],
        [KeyboardButton(text="Bosh sahifa")],
    ],
    resize_keyboard=True
)




kutubxona = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kutubxonachimisiz")],
        [KeyboardButton(text="Bosh sahifa")],
    ],
    resize_keyboard=True
)









bosh = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Bosh sahifa")],
    ],
    resize_keyboard=True
)