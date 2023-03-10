from telegram import ReplyKeyboardMarkup, KeyboardButton
import requests


def valyuta(get):
    log['state'] = 3
    url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
    response = requests.get(url)
    for i in response.json():
        if i['CcyNm_UZ'] == get:
            st = f"Nomi: {i['CcyNm_UZ']}\nQiymati: {i['Rate']}\nDifferansiyalligi: {i['Diff']}"
            return st


log = {'state': 0, 'dona': 1}


def button(step=None):
    btn = []
    if step == "button":
        url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
        response = requests.get(url).json()
        for i in range((log['dona'] - 1) * 9, log['dona'] * 9, 3):
            btn.append([
                KeyboardButton(response[i]['CcyNm_UZ']), KeyboardButton(response[i - 2]['CcyNm_UZ']),
                KeyboardButton(response[i - 1]['CcyNm_UZ'])
            ])
        btn.append([KeyboardButton("Next β­")])

    elif step == "Next β­":
        url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
        response = requests.get(url).json()
        for i in range((log['dona'] - 1) * 9, log['dona'] * 9, 3):
            btn.append([
                KeyboardButton(response[i]['CcyNm_UZ']), KeyboardButton(response[i - 2]['CcyNm_UZ']),
                KeyboardButton(response[i - 1]['CcyNm_UZ'])
            ])
        btn.append([KeyboardButton("π Back"), KeyboardButton("Next β­")])

    elif step == "π Back":
        url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
        response = requests.get(url).json()
        for i in range((log['dona'] - 1) * 9, log['dona'] * 9, 3):
            btn.append([
                KeyboardButton(response[i]['CcyNm_UZ']), KeyboardButton(response[i - 2]['CcyNm_UZ']),
                KeyboardButton(response[i - 1]['CcyNm_UZ'])
            ])
        btn.append([KeyboardButton("π Back"), KeyboardButton("Next β­")])

    elif step == "lang":
        btn = [
            [KeyboardButton("πΊπΏUZ"), KeyboardButton("π·πΊRU")]
        ]
    return ReplyKeyboardMarkup(btn, resize_keyboard=True)


def start(update, context):
    log['state'] = 1
    update.message.reply_text("Assalomu aleykum", reply_markup=button("button"))


def message_handler(update, context):
    msg = update.message.text
    if msg == "Next β­":
        log['dona'] = 2
        log['dona'] = log.get("dona", 1) + 1
        update.message.reply_text(f"Valyutalardan birini tanlang", reply_markup=button("Next β­"))
    elif msg == "π Back":
        log["dona"] = log.get("dona", 1) - 1
        update.message.reply_text(f"Valyutalardan birini tanlang", reply_markup=button("π Back"))
    else:
        update.message.reply_text(f"Markaziy bankning bugungi valyuta kursi:\n{valyuta(msg)}")
