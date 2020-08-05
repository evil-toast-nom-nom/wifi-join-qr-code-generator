# WiFi join QR code generator
Have you ever wanted to just share your WiFi network details with your guests? This little script
makes that possible with a quick QR code scan.  
Since it is easy to steal people's WiFi passwords with an online site, this is completely offline for your safety.

## How to use it
This has been tested with anything > python 3.6.5, so if you don't have a version greater than 3.6.0 please
[install it](https://www.python.org/downloads/).  
Checking your version can be done by typing:  
```python --version```  
You should see something like this:  
```Python 3.6.5```  

### Installing the requirements
Just run:
```python -m pip install -r requirements.txt```

### Configure the script
Edit the following values:  
```"my wifi name"```  
```"my wifi password"```  
```"WPA"``` if you use something other than WPA  
Then just run it!  

## Credits
A hat tip to the guys who made the [qrcode](https://pypi.org/project/qrcode/) and [Pillow](https://pypi.org/project/Pillow/) modules.






