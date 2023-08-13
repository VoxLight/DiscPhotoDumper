import nextcord
from .utils import up_dir
import json
import os


client = nextcord.Client(intents=nextcord.Intents.all())
with open(os.path.join(up_dir(__file__, 2), 'config.json')) as conf_f:
    config = json.load(conf_f)


@client.event
async def on_ready():
    print("ready")


client.run(config['token'])