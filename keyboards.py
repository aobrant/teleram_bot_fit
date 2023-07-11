from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton

inline_btn_01 = InlineKeyboardButton('Add BioBits 🫳🏻 ', callback_data='btn_add_bits')
inline_btn_02 = InlineKeyboardButton('View BioBits (under construction)', callback_data='btn_view_bits')
inline_btn_03 = InlineKeyboardButton('Analyze your BioBits 📊 (under construction)', callback_data='btn_analyze_bits')
inline_btn_04 = InlineKeyboardButton('Set reminders ⏰(under construction)', callback_data='btn_set_bits')

inline_btn_05 = InlineKeyboardButton('Sports ', callback_data='btn_sports')
inline_btn_06 = InlineKeyboardButton('Drinks ', callback_data='btn_drinks')
inline_btn_07 = InlineKeyboardButton('Sleep quality ', callback_data='btn_sleep')
inline_btn_08 = InlineKeyboardButton('1️⃣', callback_data='btn_s1')
inline_btn_09 = InlineKeyboardButton('2️⃣', callback_data='btn_s2')
inline_btn_10 = InlineKeyboardButton('3️⃣', callback_data='btn_s3')
inline_btn_11 = InlineKeyboardButton('4️⃣', callback_data='btn_s4')
inline_btn_12 = InlineKeyboardButton('5️⃣', callback_data='btn_s5')
inline_btn_13 = InlineKeyboardButton('Coffee (add 1 cup) ', callback_data='btn_coffee')
inline_btn_14 = InlineKeyboardButton('Daily water consumption (add 1 liter)', callback_data='btn_water')
inline_btn_15 = InlineKeyboardButton('Blood pressure (XX / YY mmHg)', callback_data='btn_pressure')
inline_btn_16 = InlineKeyboardButton('Weight (kg)', callback_data='btn_weight')

inline_btn_16 = InlineKeyboardButton('Walking (km)', callback_data='btn_walk')
inline_btn_17 = InlineKeyboardButton('Running (km)', callback_data='btn_run')
inline_btn_18 = InlineKeyboardButton('Cycling (km)', callback_data='btn_cycling')
inline_btn_19 = InlineKeyboardButton('Fitness / Gym workouts (hours)', callback_data='btn_gym')
inline_btn_20 = InlineKeyboardButton('Swimming (hours)', callback_data='btn_swim')
inline_btn_21= InlineKeyboardButton('Trekking / Hiking (km)', callback_data='btn_hike')
inline_btn_22 = InlineKeyboardButton('Tennis (hours)', callback_data='btn_tennis')

inline_btn_23 = InlineKeyboardButton('Beer (1 cup)', callback_data='btn_beer')
inline_btn_24 = InlineKeyboardButton('Wine (1 glass)', callback_data='btn_wine')
inline_btn_25 = InlineKeyboardButton('Vodka (1 shot)', callback_data='btn_vodka')
inline_btn_26 = InlineKeyboardButton('Whiskey (1 shot)', callback_data='btn_whiskey')
inline_btn_27 = InlineKeyboardButton('Rum (1 shot)', callback_data='btn_rum')
inline_btn_28 = InlineKeyboardButton('Tequila( 1 shot)', callback_data='btn_tequila')
inline_btn_29 = InlineKeyboardButton('Gin (1 shot)', callback_data='btn_gin')

inline_btn_30 = InlineKeyboardButton('⬅️ Back)', callback_data='back')
inline_btn_31 = InlineKeyboardButton('⛪ Home)', callback_data='home')

inline_kb_0 = InlineKeyboardMarkup(row_width=2).add(inline_btn_01, inline_btn_02)
inline_kb_0.add(inline_btn_03)
inline_kb_0.add(inline_btn_04)

inline_kb_1 = InlineKeyboardMarkup(row_width=2).add(inline_btn_05, inline_btn_06)
inline_kb_1.add(inline_btn_07)
inline_kb_1.row(inline_btn_08, inline_btn_09, inline_btn_10, inline_btn_11, inline_btn_12)
inline_kb_1.add(inline_btn_13, inline_btn_14)
inline_kb_1.add(inline_btn_15)
inline_kb_1.add(inline_btn_16)

inline_kb_2 = InlineKeyboardMarkup(row_width=1).add(inline_btn_16, inline_btn_17, inline_btn_18, inline_btn_19,
                                                    inline_btn_20, inline_btn_21, inline_btn_22, inline_btn_31)


inline_kb_3 = InlineKeyboardMarkup(row_width=3).add(inline_btn_23, inline_btn_24, inline_btn_25, inline_btn_26,
                                                    inline_btn_27, inline_btn_28, inline_btn_29, inline_btn_31)

