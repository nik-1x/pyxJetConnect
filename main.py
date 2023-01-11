from xjetpy import pyxJet
from xjetpy.constants import xJetNet
import asyncio
import json


api = pyxJet(
    api_key="63bf1a528163ac6458e1e2d9fcc2042e4810a0ebbd6877c0120569bd65be044e7511555c9465ef1f900e0e59",
    private_key="d01feeb0f81f7210fdf07284917df29c734336a833ac9ea2682792019ff690d9", 
    mainnet=xJetNet.TESTNET
)


async def main():

    res = await api.invoice_status()


asyncio.run(main())