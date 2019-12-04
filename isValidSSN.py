import re

def isValidSSN(myStr):
    # check if format is ###-##-####
    return bool(re.fullmatch('\d{3}-\d{2}-\d{4}', myStr))
