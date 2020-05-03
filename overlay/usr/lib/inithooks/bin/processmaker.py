#!/usr/bin/python3
"""Set ProcessMaker admin password and email

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively

"""

import sys
import getopt
import inithooks_cache
import hashlib

from dialog_wrapper import Dialog
from mysqlconf import MySQL

def usage(s=None):
    if s:
        print("Error:", s, file=sys.stderr)
    print("Syntax: %s [options]" % sys.argv[0], file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError as e:
        usage(e)

    password = ""
    email = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "ProcessMaker Password",
            "Enter new password for the ProcessMaker 'admin' account.")

    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "ProcessMaker Email",
            "Enter email address for the ProcessMaker 'admin' account.",
            "admin@example.com")

    inithooks_cache.write('APP_EMAIL', email)

    hashpass = hashlib.md5(password.encode('utf8')).hexdigest()

    m = MySQL()

    for table in ('USERS', 'RBAC_USERS'):
        m.execute(f'UPDATE wf_workflow.{table} SET USR_PASSWORD=%s WHERE USR_USERNAME=\"admin\";', (hashpass,))
        m.execute(f'UPDATE wf_workflow.{table} SET USR_EMAIL=%s WHERE USR_USERNAME=\"admin\";', (email,))


if __name__ == "__main__":
    main()

