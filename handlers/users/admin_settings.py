from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from keyboards.inline.admin_menu import *
from loader import dp
from states.admin_states import *
from utils.db_api.db_commands import update_settings_num, update_settings_p2p, update_settings_token, \
    update_qiwi_secret, update_settings_log_channel, update_settings_req_channel


@dp.callback_query_handler(text="edit_settings")
async def choose_settings(call: CallbackQuery):
    await call.message.edit_caption("<b>Выберите то, что хотите изменить</b>", reply_markup=admin_settings_menu)


@dp.callback_query_handler(text_startswith="choose_settings:")
async def choose_settings(call: CallbackQuery):
    option = call.data.split(":")[1]
    keyboard = wallet_settings_menu if option == "wallet" else gift_settings_menu
    await call.message.edit_caption("<b>Выберите то, что хотите изменить</b>", reply_markup=keyboard)


@dp.callback_query_handler(text_startswith="settings:")
async def choose_settings(call: CallbackQuery, state: FSMContext):
    settings_type = call.data.split(":")[1]
    await EditSettingsState.E1.set()
    msg_to_edit = await call.message.edit_caption("<b>Введите новое значение:</b>", reply_markup=back_admin)
    await state.update_data(msg_to_edit=msg_to_edit, settings_type=settings_type)


@dp.message_handler(state=EditSettingsState.E1)
async def edit_settings(message: Message, state: FSMContext):
    data = await state.get_data()
    msg_to_edit, settings_type = data.get("msg_to_edit"), data.get("settings_type")
    if settings_type == "num":
        await update_settings_num(message.text)
    elif settings_type == "p2p":
        await update_settings_p2p(message.text)
    elif settings_type == "token":
        await update_settings_token(message.text)
    await message.delete()
    await msg_to_edit.edit_caption("<b>Готово!\nНастройка изменена</b>", reply_markup=back_admin)


@dp.callback_query_handler(text="edit_channel_id")
async def edit_commission(call: CallbackQuery, state: FSMContext):
    msg_to_edit = await call.message.edit_caption("<b>Напишите ID канала.</b>",
                                                  reply_markup=back_admin)
    await EditChannelID.EC1.set()
    await state.update_data(msg_to_edit=msg_to_edit)


@dp.message_handler(state=EditChannelID.EC1)
async def receive_com(message: Message, state: FSMContext):
    com = message.text
    data = await state.get_data()
    msg_to_edit = data.get("msg_to_edit")
    await update_settings_log_channel(com)
    await message.delete()
    await msg_to_edit.edit_caption("ID канала изменен.", reply_markup=back_admin)


@dp.callback_query_handler(text="edit_qiwi_secret")
async def edit_commission(call: CallbackQuery, state: FSMContext):
    msg_to_edit = await call.message.edit_caption("<b>Напишите QIWI SECRET KEY.</b>",
                                                  reply_markup=back_admin)
    await EditSecretKey.EC1.set()
    await state.update_data(msg_to_edit=msg_to_edit)


@dp.message_handler(state=EditSecretKey.EC1)
async def receive_com(message: Message, state: FSMContext):
    com = message.text
    data = await state.get_data()
    msg_to_edit = data.get("msg_to_edit")
    await update_qiwi_secret(com)
    await message.delete()
    await msg_to_edit.edit_caption("QIWI SECRET KEY изменен.", reply_markup=back_admin)


@dp.callback_query_handler(text="edit_log_channel")
async def edit_commission(call: CallbackQuery, state: FSMContext):
    msg_to_edit = await call.message.edit_caption("<b>Напишите ID чата для логов.</b>",
                                                  reply_markup=back_admin)
    await EditLogChannel.EC1.set()
    await state.update_data(msg_to_edit=msg_to_edit)


@dp.message_handler(state=EditLogChannel.EC1)
async def receive_com(message: Message, state: FSMContext):
    com = message.text
    data = await state.get_data()
    msg_to_edit = data.get("msg_to_edit")
    await update_settings_log_channel(com)
    await message.delete()
    await msg_to_edit.edit_caption("ID чата для логов изменен.", reply_markup=back_admin)


@dp.callback_query_handler(text="edit_req_channel")
async def edit_commission(call: CallbackQuery, state: FSMContext):
    msg_to_edit = await call.message.edit_caption("<b>Напишите ID чата для обязательной подписки.</b>",
                                                  reply_markup=back_admin)
    await EditReqChannel.EC1.set()
    await state.update_data(msg_to_edit=msg_to_edit)


@dp.message_handler(state=EditReqChannel.EC1)
async def receive_com(message: Message, state: FSMContext):
    com = message.text
    data = await state.get_data()
    msg_to_edit = data.get("msg_to_edit")
    await update_settings_req_channel(com)
    await message.delete()
    await msg_to_edit.edit_caption("ID чата для обязательной подписки изменен.", reply_markup=back_admin)
