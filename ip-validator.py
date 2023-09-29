import re
regex="^(([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([1-9]?[0-9]|1[0-9][0-9]|2[0-5][0-5])?"
def check_ip(Ip):
    if(re.search(regex,Ip)):
        print("Ip address is valid")
    else:
        print("Ip address is unvalid")
if __name__== '__main__'  :
        Ip="192.168.0.1"
        check_ip(Ip)
        Ip="0.0.0.0"
        check_ip(Ip)
        Ip = "326.254.12.3"
        check_ip(Ip)
        Ip = "-1.22.255.2"
        check_ip(Ip)
