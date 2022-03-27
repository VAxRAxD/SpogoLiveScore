import environ

from SpogoScore.settings import SECRET_KEY

env = environ.Env()
environ.Env.read_env()

SECRET_KEY=env('SECRET_KEY')
REDDIS_PORT=env('REDDIS_PORT')
API_KEY=env('API_KEY')