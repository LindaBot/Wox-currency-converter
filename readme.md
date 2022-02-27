# Wox Currency Converter - Wox Plugin for Python

An extension that sits on top of [Wox](http://www.wox.one/) for instant currency conversion. 

Example:

<img width="468" alt="image" src="https://user-images.githubusercontent.com/29315719/155868584-d4971b8d-276b-4504-af8d-7155c7af5e51.png">

<img width="470" alt="image" src="https://user-images.githubusercontent.com/29315719/155868589-b0d82e8a-1d54-43af-9966-23e327fa9e2a.png">

How to use this extension:
* Make sure you have wox installed: [The main wox program can be found here](http://www.wox.one/)
* Download this repo and add the extension using [this guide here](https://github.com/Wox-launcher/Wox)
* After you've placed this repo into the extension directory, you will need to configure the [CoinMarketCap API key](https://coinmarketcap.com/api/)
* To do this, create a new file called `config.json` and put in the following JSON, replace the value with your own API key.
```JSON
{
    "CMC_API_KEY": "YOUR_API_KEY"
}
```
* Test it by invoking wox and type in `500usd to nzd`.
