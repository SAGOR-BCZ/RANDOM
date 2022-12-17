import os, sys
os.system('git pull')
try:
    __import__("pro_enc").ud()
except Exception as e:
    exit(str(e))
