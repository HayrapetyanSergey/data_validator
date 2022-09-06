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
    my_date = "^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
    if re.search(my_date, data):
        return True
    return False

def is_mobile(data):
    rule = re.compile("^[0|+374]+[41|43|44|55|77|91|93|94|95|97|98]+[0-9]{6}$")
    if  re.search(rule, data):
        return True
    return False

def is_website_URL(data):
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
    my_url = re.compile(regex)
    if (data == None):
        return False
    if(re.search(my_url, data)):
        return True
    else:
        return False 