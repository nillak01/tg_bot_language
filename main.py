from config_data.config import load_config


config = load_config('D:/GitHub/Repositories/tg_bot_template/.env')

# Сохраняем токен в переменную bot_token
bot_token = config.tg_bot.token

# Сохраняем ID админа в переменную superadmin
superadmin = config.tg_bot.admin_ids[0]

print(bot_token, '\n', superadmin)
