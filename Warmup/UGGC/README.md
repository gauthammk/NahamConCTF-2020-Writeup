# UGGC

Points : 30

## Solution

The title hints at a ROT13 cipher. When we open up the page and go to the cookies, we can see a cookie called 'user' with a ROT13 encoded version of the username as the value. So the cookie value 'a' is translated to 'n', 'b' to 'o' and so on. Since we have to login as 'admin', we can edit the cookie to represent the ROT13 version of 'admin' i.e 'nqzva'. This gives us the flag.

Flag : `flag{H4cK_aLL_7H3_C0okI3s}`
