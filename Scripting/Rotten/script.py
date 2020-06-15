import pwn

# set up remote connection
r = pwn.remote('jh2i.com', 50034)
msg = ''
abc = "abcdefghijklmnopqrstuvwxyz"
# secret = [abc[(abc.find(c)+12) % 26] for c in cleartxt]

while True:
    msg = r.recv().decode('utf-8')
    shift = ord('s') - ord(msg[0])
    secret = ''
    for c in msg:
        if c in abc:
            secret += abc[(abc.find(c)+shift) % 26]
        else:
            secret += c
    r.send(secret)
    print(secret)
