import re

def persian_only(s):
    return "".join(re.findall(r"[\u0600-\u06FF]+", s))
