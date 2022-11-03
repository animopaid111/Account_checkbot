from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ( CommandHandler, Filters, MessageHandler, Updater)
from message import Editmessage, Sendmessage, logger
from Checks.Altbalaji import altbalaji_helper
from Checks.hoichoi import hoichoi_helper
from Checks.voot import Voot_helper
from Checks.zee5 import zee_helper
from Miscellaneous.Scraper import pastebin, text_scraper, throwbin
import os


bot_token = os.environ.get('TG_BOT_TOKEN')
startmessage = [[
		InlineKeyboardButton(
			"📜 𝐆𝐮𝐢𝐝𝐞",
			url='https://telegra.ph/Guide-to-Use-This-Bot-11-03'
		),
        InlineKeyboardButton(
			"🧑‍💻 𝐃𝐞𝐯",
			url='https://t.me/PiroAyush'
		)
        ]]


def start(update, context):
    info = update.effective_user
    print(info)
    chat_id = info.id
    userid= info['username']
    text = f'🙋‍♂ Hᴇʟʟᴏ @{userid},\n\n~ I am Multi Account checker \n\n~ To see my commands - /cmds\n━━━━━━━━━━━━━━━━━━\n\n✅ Available Checkers\n\n┏━━━━━━━━━━\n┠᪥ Zee5 Checker\n┠᪥ Voot Checker\n┠᪥ Alt balaji checker\n┠᪥ hoichoi checker\n┠━━━━━━━━━━\n\nBot By - [𓆩𓊈𝗣𝗜𝗥𝗢 𝗔𝗬𝗨𝗦𝗛𓊉𓆪 </>]\n@PiroAyush\n━━━━━━━━━━━━━━━━━━'
    Sendmessage(chat_id, text, reply_markup=InlineKeyboardMarkup(startmessage))
    return

    
def combos_spilt(combos):
    split = combos.split('\n')
    return split


def help(update, context):
    chat_id = update.message.chat_id
    text = "<b>Top commands:\n\nZee Checker | !zee\nStatus: ✅ ON\n\nVoot Checker | !voo\nStatus: ✅ ON\n\nAlt Balaji Checker | !alt\nStatus: ✅ ON\n\nHoichoi Checker | !hoi\nStatus: ✅ ON\n*combo Here Means Email:Password\nCombination,':' Is Important.\n\nMiscellaneous:-\n!pst~space~title|text - to paste text on\nThrowbin.io and get paste link(If you don't\nwant to give title then skip it just send the text)\n\n~ Bot by - [𓆩𓊈𝗣𝗜𝗥𝗢 𝗔𝗬𝗨𝗦𝗛𓊉𓆪 </>]\n@PiroAyush</b>"
    Sendmessage(chat_id, text, reply_markup= InlineKeyboardMarkup(startmessage))

def duty(update, context):
    chat_id = update.message.chat_id
    text =  update.message.text.split(' ', 1)
    if text[0] == '!alt':
        if '\n' in text[1]:
            simple = combos_spilt(text[1])
            for i in simple:
                altbalaji_helper(chat_id, i)
            Sendmessage(chat_id, 'Completed')
        else:
            altbalaji_helper(chat_id, text[1])
    elif text[0] == '!voo':
        if '\n' in text[1]:
            simple = combos_spilt(text[1])
            for i in simple:
                Voot_helper(chat_id, i)
            Sendmessage(chat_id, 'Completed')
        else:
            Voot_helper(chat_id, text[1])
    elif text[0] == '!hoi':
        if '\n' in text[1]:
            simple = combos_spilt(text[1])
            for i in simple:
                hoichoi_helper(chat_id, i)
            Sendmessage(chat_id, 'Completed')
        else:
            hoichoi_helper(chat_id, text[1])
    elif text[0] == '!zee':
        if '\n' in text[1]:
            simple = combos_spilt(text[1])
            for i in simple:
                zee_helper(chat_id, i)
            Sendmessage(chat_id, 'Completed')
        else:
            zee_helper(chat_id, text[1])
    elif text[0] == '!pst':
            try:
                throwbin(chat_id, text[1])
            except IndexError:
                Sendmessage(chat_id, "<i>Somethings wrong with your format!</i>")
    else:
        logger.info('Unknown Command')


def scraperdfnc(update, context):
    msg = update.message.text
    status_msg = update.message
    chat_id = status_msg.chat_id
    try:
        if 'pastebin' in msg:
            link = msg.split(' ')[1]
            pastebin(chat_id,link)
        else:
            scrape_text = status_msg['reply_to_message']['text']
            text_scraper(chat_id, scrape_text)
    except:
        Sendmessage(chat_id, 'Only Supports pastebin, please check if you send paste bin link')

def main():
    updater = Updater(
        bot_token,
        use_context=True
    )
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, duty))
    dp.add_handler(CommandHandler("scrape", scraperdfnc))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    logger.info("Bot Started!!!")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
