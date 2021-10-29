# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
Ini adalah Bot Toko Berkas Permanen! Kirimi saya file apa pun, saya akan menyimpannya di Database saya. Juga berfungsi untuk saluran.
Tambahkan saya ke saluran sebagai Admin dengan Izin Edit, saya akan menambahkan Simpan File Unggahan di Saluran & tambahkan Tautan Tombol yang Dapat Dibagikan.

🤖 **My Name:** [Bot](https://t.me/{BOT_USERNAME})

🧑🏻‍💻 **Developer:** [Feri](https://t.me/xrinhere)

👥 **Channel:** [Gabung](https://t.me/pemersatubangsaviralnih)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** [Feri](https://t.me/xrinhere)

**WAJIB JOIN CHANNEL >> @pemersatubangsaviralnih BIAR VIDEO MUNCUL! .**
"""
	HOME_TEXT = """
Hai, [{}](tg://user?id={})\n\n Member

Kirimi saya file apa pun, saya akan memberi Anda Tautan yang Dapat Dibagikan secara permanen.
"""
