import os
from pydo import Client
from decouple import config


TOKEN = config("DIGITALOCEAN_TOKEN")


class DropletController:
    def __init__(self):
        self.client = Client(TOKEN)

    def power_cycle_droplet(self):
        resp = self.client.droplets.list()
        droplet_id = resp.get("droplets")[0].get("id")
        req = {"type": "reboot"}
        self.client.droplet_actions.post(droplet_id=droplet_id, body=req)
        return

    def list_all_droplets(self):
        return self.client.droplets.list()
