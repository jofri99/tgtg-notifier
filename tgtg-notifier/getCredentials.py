from tgtg import TgtgClient

client = TgtgClient(email="tgtgapi@googlemail.com")
client.get_credentials()
client.print()