# Copyright (c) 2025 devgagan : https://github.com/devgaganin.
# Licensed under the GNU General Public License v3.0.
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv
load_dotenv()

# ════════════════════════════════════════════════════════════════════════════════
# ░ CONFIGURATION SETTINGS
# ════════════════════════════════════════════════════════════════════════════════

# VPS --- FILL COOKIES 🍪 in """ ... """ 
INST_COOKIES = """
# write up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

# ─── BOT / DATABASE CONFIG ──────────────────────────────────────────────────────
API_ID       = os.getenv("API_ID", "28961091")
API_HASH     = os.getenv("API_HASH", "fa3796dbdec1efdf151aca5f14815d06")
BOT_TOKEN    = os.getenv("BOT_TOKEN", "8435522221:AAFuO-TftQhCb56xBuy3GgboQXBvEsuSqFQ")
MONGO_DB     = os.getenv("MONGO_DB", "mongodb+srv://talaridinesh2005:uPZDnv16yv3sAl23@cluster0.veecfly.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME      = os.getenv("DB_NAME", "telegram_downloader")

# ─── OWNER / CONTROL SETTINGS ───────────────────────────────────────────────────
OWNER_ID     = list(map(int, os.getenv("OWNER_ID", "1573111356").split()))  # space-separated list
STRING       = os.getenv("STRING", None)  # optional session string
LOG_GROUP    = int(os.getenv("LOG_GROUP", "-1003140612592"))
FORCE_SUB    = int(os.getenv("FORCE_SUB", "-1002603005939"))

# ─── SECURITY KEYS ──────────────────────────────────────────────────────────────
MASTER_KEY   = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq")  # session encryption
IV_KEY       = os.getenv("IV_KEY", "s7Yx5CpVmE3F")  # decryption key

# ─── COOKIES HANDLING ───────────────────────────────────────────────────────────
YT_COOKIES   = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)

# ─── USAGE LIMITS ───────────────────────────────────────────────────────────────
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "1"))
PREMIUM_LIMIT  = int(os.getenv("PREMIUM_LIMIT", "500"))

# ─── UI / LINKS ─────────────────────────────────────────────────────────────────
JOIN_LINK     = os.getenv("JOIN_LINK", "https://t.me/Team_TD_Link")
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "https://t.me/Team_TD_Link")

# ════════════════════════════════════════════════════════════════════════════════
# ░ PREMIUM PLANS CONFIGURATION
# ════════════════════════════════════════════════════════════════════════════════

P0 = {
    "d": {
        "s": int(os.getenv("1", 1)),
        "du": int(os.getenv("30", 7)),
        "u": os.getenv("50", "Daily"),
        "l": os.getenv("1", "Daily"),
    },
    "w": {
        "s": int(os.getenv("200", 3)),
        "du": int(os.getenv("100", 1)),
        "u": os.getenv("PLAN_W_", "weeks"),
        "l": os.getenv("PLAN_W_L", "Weekly"),
    },
    "m": {
        "s": int(os.getenv("500", 5)),
        "du": int(os.getenv("500", 1)),
        "u": os.getenv("PLAN_M_U", "month"),
        "l": os.getenv("PLAN_M_L", "Monthly"),
    },
}

# ════════════════════════════════════════════════════════════════════════════════
# ░ DEVGAGAN
# ════════════════════════════════════════════════════════════════════════════════




