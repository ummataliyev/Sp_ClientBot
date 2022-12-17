from environs import Env

env = Env()
env.read_env()

CONFIG: dict = {
    "api_id": env.str("API_ID"),
    "api_hash": env.str("API_HASH"),
    "name": env.str("NAME", default="anon"),
}

BLOCK_LIST: list = env.list("BLOCK_LIST")
AVIABLE_USER: int = 2105729169
