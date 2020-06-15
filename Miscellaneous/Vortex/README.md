# Vortex

Points : 75

## Solution

After connecting to the service, we see a seemingly infinite amount of garbage values being thrown out. So, the most logical step is to check for strings and check if it contains the flag. We can pipe the output to strings and then search for the flag like so :

```bash
nc jh2i.com 50017 | strings | grep flag
```

After about a minute, the script spits out out flag.

Flag :`nc jh2i.com 50017 | strings | grep flag`
