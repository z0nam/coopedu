from os import environ

SESSION_CONFIG_DEFAULTS = {"real_world_currency_per_point": 90, "participation_fee": 5000}
SESSION_CONFIGS = [
    {
        "name": "dictator",
        "display_name": "독재자게임",
        "num_demo_participants": 2,
        "app_sequence": ["dictator"],
        "my_key": "",
    },{
        "name": "trust",
        "display_name": "신뢰게임",
        "num_demo_participants": 2,
        "app_sequence": ["trust"],
        "my_key": "",
    },{
        "name": "public_goods",
        "display_name": "공공재게임",
        "num_demo_participants": 3,
        "app_sequence": ["public_goods"],
        "my_key": "",
    }
]
LANGUAGE_CODE = "ko"
REAL_WORLD_CURRENCY_CODE = "KRW"
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ""
ROOMS = []

ADMIN_USERNAME = "admin"
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")

SECRET_KEY = "blahblah"

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ["otree"]
