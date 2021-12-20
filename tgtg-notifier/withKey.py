from tgtg import TgtgClient
import json
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
USER_ID = os.getenv('USER_ID')

class Item:
    def __init__(self, id, available,store):
        self.id = id
        self.available = available
        self.store = store
    def printItem(self):
        print(self.id)
        print(self.available)
        print(self.store)

client = TgtgClient(access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN, user_id=USER_ID)
output = client.get_item(item_id=21129)

id = output["item"]["item_id"]
itemsAvailable = output["items_available"] 
store = output["display_name"]


item = Item(id,itemsAvailable,store)




item.printItem()