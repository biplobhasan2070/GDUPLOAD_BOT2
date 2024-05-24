import os
import logging

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


ENV = bool(os.environ.get('ENV', False))
try:
  if ENV:
    BOT_TOKEN = ('5436508081:AAEaiqF2JxmFf3RLZtybQh0QzqvOSVtyLYA')
    APP_ID = ('5310709')
    API_HASH = ('63a546bdaf18e2cbba99f87b4274fa05')
    DATABASE_URL = ('postgres://nfs2145_user:LVactZnW7jLXoCmoqdtOamBccCOvT8nt@dpg-cp809a4f7o1s73em2u1g-a.oregon-postgres.render.com/nfs2145')
    SUDO_USERS = ('1667558324')
    SUPPORT_CHAT_LINK = ('https://t.me/nafisfuad1')
    DOWNLOAD_DIRECTORY = ("./downloads/")
    G_DRIVE_CLIENT_ID = ("534301163350-3pq3llm37fkqaev61hbmktssi0fq8sb9.apps.googleusercontent.com")
    G_DRIVE_CLIENT_SECRET = ("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")
  else:
    from bot.config import config
    BOT_TOKEN = ('5436508081:AAEaiqF2JxmFf3RLZtybQh0QzqvOSVtyLYA')
    APP_ID = ('5310709')
    API_HASH = ('63a546bdaf18e2cbba99f87b4274fa05')
    DATABASE_URL = ('postgres://nfs2145_user:LVactZnW7jLXoCmoqdtOamBccCOvT8nt@dpg-cp809a4f7o1s73em2u1g-a.oregon-postgres.render.com/nfs2145')
    SUDO_USERS = ('1667558324')
    SUPPORT_CHAT_LINK = ('https://t.me/nafisfuad1')
    DOWNLOAD_DIRECTORY = ("./downloads/")
    G_DRIVE_CLIENT_ID = ("534301163350-3pq3llm37fkqaev61hbmktssi0fq8sb9.apps.googleusercontent.com")
    G_DRIVE_CLIENT_SECRET = ("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")
  SUDO_USERS = list("1667558324")
  SUDO_USERS.append(939425014)
  SUDO_USERS = list(set(SUDO_USERS))
except KeyError:
  LOGGER.error('One or more configuration values are missing exiting now.')
  exit(1)
