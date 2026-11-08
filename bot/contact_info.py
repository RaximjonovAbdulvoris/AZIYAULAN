"""Public AZIYA TAXI details, shared by menu and applicant notifications."""
import os
from html import escape

PHONE = os.environ.get('CONTACT_PHONE', '').strip() or '+998 94 555 79 79'
ADMIN = os.environ.get('CONTACT_TELEGRAM', '').strip().lstrip('@') or 'WBtaxiAziya'
CHANNEL = os.environ.get('CONTACT_CHANNEL', '').strip().lstrip('@') or 'wbtaxi_aziya'
ADDRESS = os.environ.get('OFFICE_ADDRESS', '').strip() or 'AZIYA TAXI ofisi — joylashuvni xaritada ko‘ring'
MAP_URL = os.environ.get('OFFICE_MAP_URL', '').strip() or 'https://yandex.uz/maps/-/CXvhFL6W'
CONTACT_FOOTER = f'📞 Aloqa: {PHONE}\n✉️ Telegram: @{ADMIN}'
CONTACT_FOOTER_HTML = escape(CONTACT_FOOTER)

INSTAGRAM_URL = 'https://www.instagram.com/wbtaxiaziya/'
