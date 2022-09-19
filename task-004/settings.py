import environ


env = environ.Env()
env_path = "./.env"
environ.Env.read_env(env_path)


API_KEY = env("API_KEY")
