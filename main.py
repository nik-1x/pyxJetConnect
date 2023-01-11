from xjetpy import pyxJet
from xjetpy.constants import xJetNet
import asyncio
import json


api = pyxJet(
    api_key="API_KEY",
    private_key="PRIVATE_KEY", 
    mainnet=xJetNet.TESTNET
)


async def main():

    me = await api.me()
    balance = await api.balance()

    print(json.dumps(me, indent=4))
    print(json.dumps(balance, indent=4))


asyncio.run(main())