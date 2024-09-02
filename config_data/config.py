from dataclasses import dataclass
from environs import Env
import logging

logging.basicConfig(
    level='INFO'
)

logger = logging.getLogger(__name__)


@dataclass
class DatabaseConfig:
    database: str         # Название базы данных
    db_host: str          # URL-адрес базы данных
    db_user: str          # Username пользователя базы данных
    db_password: str      # Пароль к базе данных


@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


def load_config(path: str | None = None) -> Config:
    # Создаем эксемпляр класса Env
    env: Env = Env()

    # Пробуем загрузить данные из .env
    try:
        # Добавляем в переменное окружение данные из .env
        env.read_env(path)

        # Возвращаем созданный эксемпляр класса Config
        return Config(
            tg_bot=TgBot(
                token=env('BOT_TOKEN'),
                admin_ids=list(map(int, (env.list('ADMIN_ID'))))
            ),
            db=DatabaseConfig(
                database=env('DATABASE'),
                db_host=env('DB_HOST'),
                db_user=env('DB_USER'),
                db_password=('DB_PASSWORD')
            )
        )
    except Exception:
        logger.error("Cant read env")
