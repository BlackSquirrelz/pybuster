import requests
import sys
import os
# Only use for good, not bad.


def load_wordlist(wordlist):
    """Loading the a list of words to iterate / brute force on a given host."""
    if not os.path.isfile(wordlist):
        print(f"{wordlist} does not  exist. Check your spelling.")
    else:
        with open(wordlist) as f:
            content = f.read().splitlines()

    subdirectories = [dir for dir in content]
    return subdirectories


def pwn_site(host, subdir):
    """Check if the site exists."""
    full_url = str(host) + "/" + str(subdir)
    r = requests.get(full_url)
    print(f"{full_url} - {r.status_code}")
    return r.status_code


if __name__ == '__main__':
    # Loading Variables
    host = sys.argv[1]
    wordlist_path = sys.argv[2]

    existing = []

    # Get Wordlist from specified folder
    words = load_wordlist(wordlist_path)
    for subsite in words:
        status = pwn_site(host, subsite)
        if status == 200:
            existing.append(subsite)
    print(existing)




