# Agent 95

Points : 50

## Solution

The title clearly hints at user agent manipulation. The page says the agent uses an older version of Windows and the title is Agent "95", so we can look up the user agent for Windows 95. I used this : <https://gist.github.com/sixman9/1486742> and found the user agent : Mozilla/4.0 (compatible; MSIE 5.0; Windows 95). Entering this as the user agent gives us the flag.

Flag : `flag{user_agents_undercover}`
