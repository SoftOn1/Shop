from environs import Env

env = Env()
env.read_env()

ADMINS = list(map(int, env.list("ADMINS")))
TOKEN = env.str("5161387783:AAEYG7kzZX5boqfheUyIjU2iDDU1qW5Gbd4")
API_KEY = env.str("8968412")
