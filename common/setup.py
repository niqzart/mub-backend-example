from os import getenv

from dotenv import load_dotenv

from __lib__.flask_fullstack import configure_sqlalchemy, Flask

load_dotenv(".env")

db_url: str = getenv("DB_LINK", "sqlite://")
db_meta, Base, sessionmaker = configure_sqlalchemy(db_url)

app: Flask = Flask(__name__, versions={"API": "0.1.0"})
app.secrets_from_env("hope it's local")
app.debug_from_env()
app.configure_cors()
