# -*- coding: utf-8 -*- 
#!/usr/bin/python

import mechanize
import re

browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()

browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.open("http://m.facebook.com/")
browser.select_form(nr=0)

browser.form['email'] = 'Facebook Kullanici Adi'
browser.form['pass'] = 'Facebook Sifreniz'
response = browser.submit()


#Numarayı alma denetimi   
while True:
   while True:
      try:
         numara = input("Ornek: 5357851212 seklinde giriniz.\nNumara :")
         if len(str(numara))==10:
            break
         else:
            print("[-]Yanlış Giriş. 10 Haneli Numarayı Giriniz.")
      except:
         print("[-]Hata! Lütfen Sayi Giriniz.")

   kaynak = browser.open("http://m.facebook.com/privacy/touch/block/?refid=31").read()
   browser.select_form(nr=1)
   browser.form['q'] = str(numara)
   response = browser.submit()
   kaynak =  response.read()

   if 'bulunamad' in kaynak:
      print("[!] Sonuc Bulunamadi. Numara :"+str(numara))
      print("-----------------------------------------------")
      sayi=10
   else:
      sonuclar = re.findall('<span class="bl">(.*?)</span></a>.*?<a href="/privacy/touch/block/confirm/\?bid=(.*?)">Engelle</a>',kaynak)
      for i in sonuclar:
         print("Ad-Soyad :"+i[0]+"\nLink : http://facebook.com/profile.php?id="+i[1])
         print("-----------------------------------------------")


