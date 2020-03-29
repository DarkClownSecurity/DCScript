#!/usr/bin/python3
# Kamis,26 Maret 2k20
# Mau Ngapain Liat Codenya
# Sengaja Ga Di Encode Buat Belajar
# DarkClownSecurity
# Klo Request Chat Coder :v
import os
red = "\033[31;1m"
green = "\033[32;1m"
yellow = "\033[33;1m"
blue = "\033[34;1m"
purple = "\033[35;1m"
cyan = "\033[36;1m"
white = "\033[37;1m"

os.system('toilet -f standard "DCScript" | lolcat')
print("{}/////////////////////////////////////////////////////////////////".format(purple))
print("{}/// {}.::Tool DCSript Untuk Membuat script Deface Simple & Keren::.{} ///".format(purple, white, purple))
print("{}/// {}Coded By : {}KOCH3NG_404                                   {} ///".format(purple, red, white, purple))
print("{}/// {}Team : {}Dark Clown Security                               {} ///".format(purple, yellow, blue, purple))
print("{}/// {}Website : {}Darkclownsecurity.com                          {} ///".format(purple, green, red, purple))
print("{}/// {}Subcribe Youtube : {}Dark Clown Security                   {} ///".format(purple, blue, yellow, purple))
print("{}/// {}Contact Me: {}+6281554363662                               {} ///".format(purple, cyan, green, purple))
print("{}/////////////////////////////////////////////////////////////////".format(purple))
print("\n")
dcscript = """
<html>
    <head>
        <meta charset="utf-8" />
        <link rel="icon" type="image/png" href="{icon}" />
        <link rel="SHORTCUT ICON" href="{icon}"><type="image/png" />
        <meta name="description" content="{desk}" />
        <meta name="keywords" content="{nick}" />
        <title>{title}</title>
        <link href="https://fonts.googleapis.com/css2?family=Iceland&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Iceberg&display=swap" rel="stylesheet">
    </head>
    <body style="background-color: {bg}">
        <center>
            <img src="{img}" height="250" width="250">
            <p><font style="font-size: 70px" color="red" face="Iceland"><b>Hacked By {nick}</b></font>
            <br><br>
        	<font style="font-size: 35px" face="Iceberg" color="white">{pesan}<br><br><marquee behavior="alternate" scrollamount="100" width="950px" style="width:950px;"> <font size="4px" color="red">______________________________________________<font size="4px" color="yellow">______________________________________________<font size="4px" color="#1CFF00">______________________________________________<font size="4px" color="#00A7FF">______________________________________________</font></font></font></font></marquee><br>
            <font style="font-size: 25px" face="Iceland" color="red"><b>Greetz:</font><font style="font-size:35px" face="Iceland" color="white" ><marquee>{friend} </marquee></font></br><marquee behavior="alternate" scrollamount="100" width="950px" style="width:950px;"> <font size="4px" color="red">______________________________________________<font size="4px" color="yellow">______________________________________________<font size="4px" color="#1CFF00">______________________________________________<font size="4px" color="#00A7FF">________________________________________</font></font></font></font></marquee><br><br><br>
        </center>
        <iframe width="0%" height="0" scrolling="no" frameborder="no" loop="true" allow="autoplay" src="{mp3}"></iframe>
        <script src="https://cdn.rawgit.com/bungfrangki/efeksalju/2a7805c7/efek-salju.js" type="text/javascript"></script>
    </body>
</html>
"""
try:
    title = str(input("{}Tulis Judul Halaman (ex: Hacked by K0CH3NG_404) => {}".format(red, green)))
    icon = str(input("{}Masukan Link Gambar Ikon (ex : https://i.ibb.co/Fm5TNnv/D-C-S.jpg) => {}".format(red, green)))
    desk = str(input("{}Tulis Deskripsi (ex : Dark Clown Security) => {}".format(red, green)))
    bg = str(input("{}Warna Background (ex : black) => {}".format(red, green)))
    nick = str(input("{}Masukan Nick Defacer => {}".format(red, green)))
    img = str(input("{}Masukan Link Gambar (jpg/png/gif)=> {}".format(red, green)))
    pesan = str(input("{}Tulis Pesan Galau :v (<br> untuk enter) => {}".format(red, green)))
    mp3 = str(input("{}Masukan Link Lagu Mp3 => {}".format(red, green)))
    friend = str(input("{}Tulis Nick Friend => {}".format(red, green)))
    output = str(input("{}Nama Script Deface (ex : meong.html) => {}".format(red, green)))
except (KeyboardInterrupt, KeyError, IOError):
    print("[!] Error Program Exited..")
    import time
    time.sleep(0.9)
    exit(1)

op = open(output, 'w')
op.write(dcscript.format(title=title, icon=icon, desk=desk, bg=bg, nick=nick, img=img, pesan=pesan, mp3=mp3, friend=friend))
op.close()

print("{}Success Create Script Deface :')".format(green))
print("{}Output : {}{}".format(green, blue, os.path.abspath(output)))
