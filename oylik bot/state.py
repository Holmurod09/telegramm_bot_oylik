from aiogram.fsm.state import State, StatesGroup

class soatlab(StatesGroup):
    toifa = State()
    dars_soati = State()
    sinf_rahbarligi = State()
    oquvchilar_soni = State()
    daftar_tekshirish = State()
    daftar_sinfi = State()
    daftar_tekshirish_soati = State()
    kabinet = State()
    sertifikat = State()
    ustama = State()


class boshlangich(StatesGroup):
    toifa = State()
    dars_soati = State()
    sinf_rahbarligi = State()
    oquvchilar_soni = State()
    daftar_tekshirish_soati = State()
    kabinet = State()
    sertifikat = State()
    ustama = State()


class yuqori(StatesGroup):
    toifa = State()
    dars_soati = State()
    sinf_rahbarligi = State()
    oquvchilar_soni = State()
    daftar_tekshirish_soati = State()
    kabinet = State()
    sertifikat = State()
    ustama = State()




class dekrat(StatesGroup):
    pul = State()



class tatil(StatesGroup):
    kuni = State()
    oylik = State()