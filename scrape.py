import random
import requests
import subprocess
import sys
import os
from lxml import html
from scrape_fail import __scrape_fail__

def __scrape_from_web__(size):
    pg_num = random.randrange(1,26)
    if(pg_num < 10):
        link = 'http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.' + str(0) + str(pg_num)
    else:
        link = 'http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.' + str(pg_num)
    try:
        page = requests.get(link)
        tree = html.fromstring(page.content)
        words = tree.xpath('//li/text()')
        random.SystemRandom().shuffle(words)
    except requests.exceptions.ConnectionError as e:
        print "These aren't the domains we're looking for."
        print "Internet connection issue defaulting to other methods" + '\n'
        __scrape_fail__(size)
    else:
        final_pass = (' '.join(w.strip() for w in words[:size])) + '\n' + '\n'
        target = open("pass.txt", 'a')
        target.write(final_pass)
        if sys.platform == "win32":
            os.startfile("pass.txt")
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "pass.txt"])
