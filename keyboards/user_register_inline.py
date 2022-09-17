from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message, ParseMode

inline_go_kb = InlineKeyboardMarkup()
inline_go_kb.add(
    InlineKeyboardButton('Go▶', callback_data='start_register')
)

inline_additional_confirm = InlineKeyboardMarkup()
inline_additional_confirm.add(
    InlineKeyboardButton("✅Yeah", callback_data='extra'),
    InlineKeyboardButton("❌No", callback_data='no_extra')
)


contact = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
contact.add(
    KeyboardButton('☎Send my number', request_contact=True),
    KeyboardButton('🙅‍♂️I prefer not to report it')
)


inline_delete_confirm = InlineKeyboardMarkup(row_width=1)
inline_delete_confirm.add(
    InlineKeyboardButton("🗑Yes, i want to clear my data", callback_data='delete_user'),
    InlineKeyboardButton('🔙Back', callback_data='no_delete')
)


async def notify_kb(msg: Message, respond):
    inline_notify = InlineKeyboardMarkup()
    inline_notify.add(
        InlineKeyboardButton('🔔Notify him/her', callback_data=respond[0])
    )
    await msg.answer(f'🔎𝙍𝙚𝙨𝙪𝙡𝙩𝙨\n'
                     f'🚗𝐂𝐚𝐫: {msg.text.upper()}\n'
                     f'📞𝐂𝐨𝐧𝐭𝐚𝐜𝐭: <code>+{respond[1]}</code>\n',
                     reply_markup=inline_notify,
                     parse_mode=ParseMode.HTML)
