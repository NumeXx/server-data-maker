# Simple Server Data Maker By NumeX
# Create a World with Code

# Import Module
import time

# Gooo
print("#-------------------------------------#")
print("[#] Author : (c) NumeX")
print("[#] Github : https://github.com/NumeXx")
print("#-------------------------------------#\n")
ip = input("[/] Enter Server IP : ")
port = input("[/] Enter Port (17091) : ")
maint = input("[/] Enter Maintenance message : ")
f = open("server_data.php", "w")
f.write(f"server|{ip}\nport|{port}\ntype|1\n#maint|{maint}\n\nbeta_server|127.0.0.1\nbeta_port|17091\n\nbeta_type|1\nmeta|localhost\nRTENDMARKERBS1001")
f.close()
time.sleep(1)
print("[~] Successfully Created...")
input("Enter any key for close...")

# (c) NumeX