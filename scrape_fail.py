import random
import sys
import subprocess
import os

def __scrape_fail__(size):
    words = list(open('text.txt'))
    target = open('pass.txt','a')
    random.SystemRandom().shuffle(words)
    target.write((' '.join(w.strip() for w in words[:size])))
    if sys.platform == "win32":
        os.startfile("pass.txt")
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, "pass.txt"])
