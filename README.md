# pyxJetAPI

## Author
- [@xJetLabs](https://github.com/xJetLabs) (forked from)
- [@nik-1x](https://www.github.com/nik-1x)
 
## Usage/Examples  
```python
api = pyxJet(
    api_key="API_KEY",
    private_key="PRIVATE_KEY", 
    mainnet=xJetNet.TESTNET # or xJetNet.MAINNET
)
```
```python
me = await api.me() # get API Application information.
balance = await api.balance() # get balance on API Application.
```

## License
[GNUv3](https://github.com/nik-1x/pyxJetAPI/blob/main/LICENSE)  
