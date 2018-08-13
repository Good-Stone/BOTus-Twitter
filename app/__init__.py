from os.path import join, dirname
from dotenv import load_dotenv
from .app import create_app

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

app = create_app()
