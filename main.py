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

    ton_address = ""
    currency = ""
    amount = 0
    expires = 0
    description = ""
    activates_count = 0
    groups_id = []
    personal_id = ""
    password = ""
    cheque_id = ""
    max_payments = 0
    invoice_id = ""

    await api.me() # get API Application information.
    await api.balance() # get balance
    await api.submit_deposit() # check for deposit
    await api.withdraw(ton_address, currency, amount) # check for deposit

    # Cheques methods
    await api.cheque_create(currency, amount, expires, description, activates_count, groups_id, personal_id, password) # create cheque
    await api.cheque_status(cheque_id) # get cheque status
    await api.cheque_list() # get cheques on account
    await api.cheque_cancel(cheque_id) # delete cheque

    # Invoice methods
    await api.invoice_create(currency, amount, description, max_payments) # create invoice
    await api.invoice_status(invoice_id) # get invoice status
    await api.invoice_list() # get invoices on account


asyncio.run(main())