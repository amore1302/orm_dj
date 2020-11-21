import os
from dotenv import load_dotenv
from environs import Env


env = Env()
env.read_env()


load_dotenv()


ENGINE = os.getenv("ENGINE")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
NAME = os.getenv("NAME")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")


DATABASES = {
    'default': {
        'ENGINE': ENGINE,
        'HOST': HOST,
        'PORT': PORT,
        'NAME': NAME,
        'USER': USER,
        'PASSWORD': PASSWORD,
    }
}

INSTALLED_APPS = ['datacenter']

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = env.bool('DEBUG', default=False)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True