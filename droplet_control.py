import os
from pydo import Client
from decouple import config


TOKEN = config("DIGITALOCEAN_TOKEN")
ID = config("DROPLET_ID")


class DropletController:
    def __init__(self):
        self.client = Client(TOKEN)

    def power_cycle_droplet(self):
        req = {"type": "enable_backups"}
        self.client.droplet_actions.post(droplet_id=ID, body=req)
        return
