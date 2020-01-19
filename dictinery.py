user={'admin': True, 'active': False, 'name': 'efi'}
prefix=""
if user['admin'] and user['active']:
    prefix = "ACTIVE-(ADMIN)"
elif user["admin"]:
    prefix="(ADMIN)"
elif user["active"]:
    prefix="ACTIVE-"
print(prefix+user["name"])
