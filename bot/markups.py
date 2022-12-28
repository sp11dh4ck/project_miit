from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


button_audit_8507 = InlineKeyboardButton("Аудитория #8507", callback_data = 'button_audit_8507')
# button_audit_8508 = InlineKeyboardButton("Аудитория #8508", callback_data = 'button_audit_8508')
# button_audit_8509 = InlineKeyboardButton("Аудитория #8509", callback_data = 'button_audit_8509')
kb_audit = InlineKeyboardMarkup(row_width=1).add(button_audit_8507)#button_audit_8508, button_audit_8509

button_back = InlineKeyboardButton("🔙 Назад", callback_data = 'button_back')
kb_back = InlineKeyboardMarkup().add(button_back)
