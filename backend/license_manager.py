import json
import random
import string
import os

LICENSE_FILE = os.path.join(os.path.dirname(__file__), 'licenses.json')

if os.path.exists(LICENSE_FILE):
    with open(LICENSE_FILE, 'r') as f:
        licenses = json.load(f)
else:
    licenses = {}

def generate_license(username):
    key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    licenses[key] = username
    with open(LICENSE_FILE, 'w') as f:
        json.dump(licenses, f)
    return key

def check_license(key):
    return key in licenses
