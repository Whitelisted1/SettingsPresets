from login import loginsignup
import time

print("To report bugs please check out the github: https://github.com/Whitelisted1/SettingsPresets")
print("My Discord: Whitelisted#9015")
time.sleep(2)
print("")

# THB I could have easily optimized this program but I feel like taking a little break haha
# Only realized how much I could have optimized it after I wrote it :/

userFileCreate = open("users.txt", 'a')
userFileCreate.close()

loginsignup()
