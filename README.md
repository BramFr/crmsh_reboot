# crmsh_reboot
Reboot when all crm (pacemaker) node(s) are online

Make script executable
```bash
# chmod +x ./crmsh_reboot.py
```

Create a cron for every node
```bash
# cat /etc/cron.d/automatic_reboot
0 5 * * 2 root python3 /path/to/crmsh_reboot.py
```

For more cron explanation look at this [site](https://crontab.guru)
