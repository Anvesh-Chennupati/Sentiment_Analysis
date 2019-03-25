import re
import emoji
from emoji import UNICODE_EMOJI
from emojimap import emojiMapping
import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)

def extract_emojis(tweet):
    emojis_list = map(lambda x: ''.join(x.split()), emoji.UNICODE_EMOJI.keys())
    rval = "U"
    r = re.compile('|'.join(re.escape(p) for p in emojis_list))
    aux = [' '.join(r.findall(s)) for s in tweet]
    for x in aux:
        for y in list(x):
            if y != ' ':
                rval = 'U+{:X}'.format(ord(y))
    return rval