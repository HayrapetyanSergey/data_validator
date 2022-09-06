from operator import truediv
import re
from datetime import datetime

def is_email(data):
    my_str = "^\w+[-_.,]?\w+[@]\w+[.]\w{2,3}$"
    if re.search(my_str, data):
        return True
    return False

def is_number(data):
    if data.isdigit():
        return True
    return False

def is_CreditCard(data):
    my_str1 = "^[\d{4}]+[ .,-_]+[\d{4}]+[ .,-_]+[\d{4}]+[ .,-_]+[\d{4}]$"
    if re.search(my_str1, data) and len(data) in (16,19) :
        return True
    return False

def is_Date(data):

    format_ddmmyyyy = "%d/%m/%Y"
    try:
        date = datetime.strptime(data, format_ddmmyyyy)
        return True
    except ValueError:
        return ("The string is not a date with format " + format_ddmmyyyy)

def is_mobile(data):
    rule = re.compile("^[0|+374]+[41|43|44|55|77|91|93|94|95|97|98]+[0-9]{6}$")
    if  re.search(rule, data):
        return True
    return False

#def is_website_URL(data):
import re
regex = re.compile(r'^((?:http|ftp)s?://)+(?:[A-Z0-9])+(.?:[A-Z]{2,6})', re.IGNORECASE)

print(re.match(regex, "https://www.example.com") is not None) # True
print(re.match(regex, "examplecom") is not None)          

#print(is_website_URL("barev,wslfjer"))       