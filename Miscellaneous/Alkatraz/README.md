# Alkatraz

Points : 100

## Solution

Upon connecting to the service, we are given a shell. By executing `ls`, we can see a certain flag.txt file. However, this shell does not let us execute common commands like `cat, awk, grep, sed etc`.

So the most logical step is to use more primitve bash methods to read the file byte by byte. These scripts get the job done.

```bash
printf '%s' "$(<flag.txt)"
```

```bash
echo "$(<flag.txt)"
```

Flag : `flag{congrats_you_just_escaped_alkatraz}`
