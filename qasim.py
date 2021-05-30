import requests
from bs4 import BeautifulSoup
import random
from time import sleep
import time
import telebot

bot = telebot.TeleBot("1885878921:AAEuWRPKSB1QODXuDPvYs3PbHNBuaxazJWs")


@bot.message_handler(commands=['start'])
def welcome_help(message):
    bot.send_message(message.chat.id, 'بوت حل اسئلة موقع Chegg ارسل رابط السؤال')


@bot.message_handler(content_types=['text'])
def send_document(message):
    if message.chat.type == 'supergroup':
        if ('https://www.chegg.com/my/account') in message.text or ('https://www.chegg.com/search') in message.text:
            bot.send_message(message.chat.id, 'الرجاء قم بارسال رابط السؤال بصورة صحيحة',
                             reply_to_message_id=message.message_id)
        elif 'chapter' in message.text:
            bot.send_message(message.chat.id, 'اجابات المصادر غير موجودة',
                             reply_to_message_id=message.message_id)
        elif message.text.startswith("https://www.chegg.com/homework-help/questions-and-answers/") or message.text.startswith("https://www.chegg.com/homework-help/"):
            url = message.text
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'cookie': 'C=0; O=0; V=1e7f2a5940700c25e90fa2d28dee03a65f03717a5b6d07.38960734; _pxvid=4db309e2-bfb9-11ea-a648-0242ac120007; _sdsat_oneTrustCookie=,0_179421,snc,0_189848,0_182337,prf,0_189849,fnc,0_182338,trg,0_182339,0_182867,0_182340,0_182341,0_182866,0_268915,0_268916,0_189806,0_189847,0_219331,0_244142,0_213057,0_219330,0_219332,0_213058,0_260705,0_213056,0_186627,101,102,; _sdsat_isAdobeOptOut=false; _sdsat_oneTrustTargetingCookie=true; _sdsat_oneTrustPerformanceCookie=true; _sdsat_maxmindCountry=Iraq; _scid=00238d8f-a252-432d-9159-e5565e7b3e28; _ga=GA1.2.496031478.1594826455; optimizelyEndUserId=oeu1619885028000r0.0016798534863158299; usprivacy=1YNY; _omappvp=bWEUBiexzpWLcKkVQI5XWKv8NqdHBK2TSlc7gO4U6wbWnyrJa6u8kouHxV8jj7kg05jUSswPUH9SNLstK41LrZZrwfZsO7GM; _ym_uid=1619885137311910967; _ym_d=1619885137; _rdt_uuid=1619885145324.e22633d3-93c3-4f64-a789-a3c2bc2e688d; _fbp=fb.1.1619885153815.1134328420; _gcl_au=1.1.1898123549.1619885157; __gads=ID=f9aab0cd3e873164:T=1619893589:S=ALNI_MaXmx_5btIQI2K4Cl-KSEYyHmFLUw; _vid=vNGYKLznCfMrCtergCaq; DFID=web|vNGYKLznCfMrCtergCaq; bc.visitor_token=6794946082859483136; _cs_c=1; omSeen-tgjg3ieouzbhy6fc0ctw=1620051477539; gidr=MA; sbm_dma=0; sbm_country=RS; _sctr=1|1621458000000; al_cell=2021-5-20-wt-main-1-control; chgcsdetaintoken=1; chgcsastoken=JAhZDkgz7vFDI1GpaiuEr0M0QVQDGclNfXjkKDyzeu20TYkiQ9WTJ1jQz2gYeoTRlj4I99G7ixdVIe8n1NKW5VEDwnTeh0z6UofMW9PT8oMiXyija-QUeb092GrnSbKP; adobeujs-optin=%7B%22aam%22%3Atrue%2C%22adcloud%22%3Atrue%2C%22aa%22%3Atrue%2C%22campaign%22%3Atrue%2C%22ecid%22%3Atrue%2C%22livefyre%22%3Atrue%2C%22target%22%3Atrue%2C%22mediaaa%22%3Atrue%2C%22videoaa%22%3Atrue%7D; _cs_id=187c707b-4c69-a726-cade-775cf9eb1c27.1620041470.3.1621528172.1621527423.1.1654205470758.Lax.0; __CT_Data=gpv=4&ckp=tld&dm=chegg.com&apv_79_www33=4&cpv_79_www33=4; PHPSESSID=d65a435d4867e05e9ceeee601b9dbad0; CSessionID=1c9de5ea-099d-406b-b331-22764d7d51f4; user_geo_location=%7B%22country_iso_code%22%3A%22IQ%22%2C%22country_name%22%3A%22Iraq%22%2C%22region%22%3A%22BG%22%2C%22region_full%22%3A%22Baghdad%22%2C%22city_name%22%3A%22Baghdad%22%2C%22locale%22%3A%7B%22localeCode%22%3A%5B%22ar-IQ%22%5D%7D%7D; AMCVS_3FE7CBC1556605A77F000101%40AdobeOrg=1; _gd1622237960795=1; CVID=29258665018562375872478304979529442280; sbm_a_b_test=1-control; CSID=1622237961382; mcid=29258665018562375872478304979529442280; schoolapi=null; _gid=GA1.2.1735757371.1622238036; chgmfatoken=%5B%20%22account_sharing_mfa%22%20%3D%3E%201%2C%20%22user_uuid%22%20%3D%3E%207edd9b9f-5206-4565-b447-cb17f4a7f524%2C%20%22created_date%22%20%3D%3E%202021-05-28T21%3A44%3A38.807Z%20%5D; _px3=25d9c98cc18282755832ae0c339030628c3665d6b1375b149543347e486a6197:QWlhjJm8LWF2ILg5r7XYOXngMqGeE15Uy1iEeWxJnAly4v4r3nWSiMPcwox+gJ5i4WW6pALQihBR6nkaCkRsJA==:1000:CV9GDPPzVi75sCrM34/DhNKtuNuYGOoOGviWo7+2QxMr+3VCgTadtZ8bqrj0A1pKqiaxoT5VMtDAEo0YkM41P81SEnHrWZI6snmVs8O6cnQRezY4hNOtP51/mhdE3fLOicdI9OP24vh2B9bsR/6Kk5Or2hutEoJF3VwdqfQ1Hc3fkSUPpObD+S48r27z/r4MkvLdKER38EZsKM7b5P6TCw==; id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI3ZWRkOWI5Zi01MjA2LTQ1NjUtYjQ0Ny1jYjE3ZjRhN2Y1MjQiLCJhdWQiOiJDSEdHIiwiaXNzIjoiaHViLmNoZWdnLmNvbSIsImV4cCI6MTYzODAwODM2OSwiaWF0IjoxNjIyMjM4MzY5LCJlbWFpbCI6ImFhc29hbmE3QGdtYWlsLmNvbSJ9.aTt87sSGIABh73qQzOGKnAZFHsqOA9pY8S9_3E0DHzgF4sW53IpDE4Z74o2GwTeuqhvpHtRBK4n5uNuowzK5W1BsyvLvbyIF3rZagMcgHHy-13QYTiq2trWM_DojKvG-YleQ18dHWasnIl5mDVJlSOMOt0mCyftOscPePQ6AtU_1HK6ElUq5_PWbrWRGibFdcCZ1oYV-d4NphAPW6UaDxqiVVpaS66RdEyP-_1fGCvk5MU9UM9Ev4RwPg9rUY7ecJbiIVzBU_XqCbBq-Ns83i7j7YrKbcWIIFGGew4UhCo_o5pQ9o1g5uy_NWk99dLOGwLdcRuS0lrt0d_y4RJEYQA; access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhUTkU0cWwxNTRxekZieTBBakxDdSJ9.eyJodHRwczovL3Byb3h5LmNoZWdnLmNvbS9jbGFpbXMvYXBwSWQiOiJOc1lLd0kwbEx1WEFBZDB6cVMwcWVqTlRVcDBvWXVYNiIsImlzcyI6Imh0dHBzOi8vY2hlZ2ctcHJvZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8N2VkZDliOWYtNTIwNi00NTY1LWI0NDctY2IxN2Y0YTdmNTI0IiwiYXVkIjpbImNoZWdnLW9pZGMiLCJodHRwczovL2NoZWdnLXByb2QudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMjIzODM2OSwiZXhwIjoxNjIyMjM5ODA5LCJhenAiOiIzVFpiaGZzWndkZUhiaG9WTXhPdlpHYjM3TWN2YzBvOCIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgYWRkcmVzcyBwaG9uZSBvZmZsaW5lX2FjY2VzcyIsImd0eSI6InBhc3N3b3JkIn0.L_rYE28yUT-oQdOro4axmqpuU34W-OpJQRoeFoVHcNGU15jgJk6ixngYC_-T67GPPeyZsOfEVPoUR7VxqGSnSbfwktksdM7Y7pNG5VK6DDd4VVfibbzshkAmu9DewDK_u9DQpQuYikNroIlbNbbuIszm6D6ib_Fu_o_doxgyTwIZ5s3OZ8FgqsvMtm24xiwlSc4bYVoWCY-amuDlNpvCDbow04MqEOM246Op4GBIuKYHj0XyQDrzY8ZZobkeFgVi7zIef-s9ulz2mZHlN7RfPl-OM9y0jRD3LQkGpOPPj3eACo9JQGSE9we-ZC5cnMAb-bug7KSaf-Srt4Clbpvxfw; access_token_expires_at=1622239809; refresh_token=ext.a0.t00.v1.MeKnVdKrC_Ew12IGfxIFlB8DyAWwI22BBREFLvgvmtBeiVzh1plRWGjg8holcAB6lTnhmj2cMBFlTgRQGtqGbSs; SU=p9468Wh5dH7_GHhNJas5tm0eJsXF12Nv2YfhET8etWepocuDA8SkvOu_koeaEc1MJwdyM-5tRX7_AtEFdI-A2hnZ3oQQuyjZS8KjssqlAbEzYeKYc0Q7njYFqp73bVE2; U=9f01cd4ecf7179f0c4b9f7311bd62dce; gid=1565637; exp=A311C%7CA803B%7CA100A%7CA184B%7CC024B%7CA560B%7CA259B%7CA207B%7CA209A%7CA212A%7CA890H%7CA448A%7CA270C%7CA966F%7CA278C%7CA935B; expkey=E19C2C144E76BC8754265777D8283DB8; intlPaQExitIntentModal=hide; _sdsat_cheggUserUUID=7edd9b9f-5206-4565-b447-cb17f4a7f524; _sdsat_authState=Hard%20Logged%20In; AMCV_3FE7CBC1556605A77F000101%40AdobeOrg=-408604571%7CMCIDTS%7C18776%7CMCMID%7C29258665018562375872478304979529442280%7CMCAAMLH-1622843208%7C6%7CMCAAMB-1622843208%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1622245608s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.6.0%7CMCCIDH%7C-215200707; chgcsdmtoken=%7B%22user_uuid%22%3A%227edd9b9f-5206-4565-b447-cb17f4a7f524%22%2C%22created_date%22%3A%222021-05-28T21%3A48%3A31.274Z%22%2C%22account_sharing_device_management%22%3A1%7D; OptanonConsent=isIABGlobal=false&datestamp=Sat+May+29+2021+00%3A50%3A01+GMT%2B0300+(%D8%A7%D9%84%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A+%D8%A7%D9%84%D8%B1%D8%B3%D9%85%D9%8A)&version=6.10.0&landingPath=NotLandingPage&groups=snc%3A1%2Cprf%3A1%2Cfnc%3A1%2Ctrg%3A1%2CSPD_BG%3A1&AwaitingReconsent=false&hosts=&consentId=8c64dfb3-587b-431c-9618-7b7ca08f7756&interactionCount=0; _px3=c8ee80636d66651a2e981b24fb52311c89cc161f1ed389403a77662c9372c0ea:Era4xKo2TIzWI6Vx6LZnzPSwMxrNZq08ukwQh1eIw3cFWf0l3tgl5ZCPuB1TcWv2GrGEhlTUK+kfGTwqZwRpNg==:1000:2TfQaQAy0YQvLb76GT6kxNVMRdA5Jme94gjk5fiF9WOPXxfXaWCPPT4PkgicFHpeLrsIGmvOAi1UNImpnQIKLWSInVmGC06lO0ebw6LmSoli6TQabCSIq5LzS05M2YeDLItXgyAQju7bqXJ6rw0J5t52PWxw7bvVRgIaa5/zcGiov2Qo9LB5DJX0HGSYfULqHjJob4bUSap6AKFm8j9g6g==; _px=Era4xKo2TIzWI6Vx6LZnzPSwMxrNZq08ukwQh1eIw3cFWf0l3tgl5ZCPuB1TcWv2GrGEhlTUK+kfGTwqZwRpNg==:1000:VVr/Ih2cxIXusju10OzGdzGwgqA83OsAMKAHZCda3kgfZbFQuazrJvno0342kHgWSaSMJLdD3dzlmXaiCn4h+jPhj505YHBuMWAG7ezYdkH3B1+HstClUfm0DIIFNM7dovuiKLPq/dwAvobg4bMKRmvDM+YGgVPtgxWLW5bbNKs9DnP/eODDSDh7trmxnrlcDEGOth4PBpLWTFQjLtJOWdyJSVJzxVl8EVbk6eNcrVaYpDkscig0rJBYB8qDbiaU74eeIyLMGuGdHxoexdROMA==; _uetsid=5b1656a0bffd11ebafc789ee45182185; _uetvid=1c70d0c0aa9711ebb3b16d960eeeb10c; _gat=1; wcs_bt=s_4544d378d9e5:1622238626; chgcsdmtoken=7edd9b9f-5206-4565-b447-cb17f4a7f524++web|vNGYKLznCfMrCtergCaq++1622238637469; s_pers=%20buFirstVisit%3Dstudy-pack%252Ccs%252Ccore%252Chelp%7C1779294569627%3B%20gpv_v6%3Dchegg%257Cweb%257Ccore%257Cmyaccount%257Cdevices%7C1622240439003%3B; s_sess=%20buVisited%3Dcs%252Ccore%3B%20s_ptc%3D0.01%255E%255E0.04%255E%255E0.00%255E%255E0.70%255E%255E7.06%255E%255E27.85%255E%255E600%255E%255E0.76%255E%255E600%3B%20cheggCTALink%3Dfalse%3B%20SDID%3D65808112A7BDA43B-4458250B3ED61F53%3B%20s_sq%3Dcheggincriovalidation%253D%252526pid%25253Dchegg%2525257Cweb%2525257Ccore%2525257Cmyaccount%2525257Cdevices%252526pidt%25253D1%252526oid%25253Dfunctionln%25252528%25252529%2525257B%2525257D%252526oidt%25253D2%252526ot%25253DSUBMIT%3B; _gali=redirect-on-remove-device-dialog; _pxff_cc=U2FtZVNpdGU9TGF4Ow==',
                'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.content, 'html.parser')
            x0 = soup.find('div', class_="answers-h2")
            if ("An expert answer will be posted here") in soup.text:
                bot.send_message(message.chat.id, 'لم يتم حل السؤال بعد  ',
                                 reply_to_message_id=message.message_id)
            else:
                url = message.text
                headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'cookie': 'C=0; O=0; V=1e7f2a5940700c25e90fa2d28dee03a65f03717a5b6d07.38960734; _pxvid=4db309e2-bfb9-11ea-a648-0242ac120007; _sdsat_oneTrustCookie=,0_179421,snc,0_189848,0_182337,prf,0_189849,fnc,0_182338,trg,0_182339,0_182867,0_182340,0_182341,0_182866,0_268915,0_268916,0_189806,0_189847,0_219331,0_244142,0_213057,0_219330,0_219332,0_213058,0_260705,0_213056,0_186627,101,102,; _sdsat_isAdobeOptOut=false; _sdsat_oneTrustTargetingCookie=true; _sdsat_oneTrustPerformanceCookie=true; _sdsat_maxmindCountry=Iraq; _scid=00238d8f-a252-432d-9159-e5565e7b3e28; _ga=GA1.2.496031478.1594826455; optimizelyEndUserId=oeu1619885028000r0.0016798534863158299; usprivacy=1YNY; _omappvp=bWEUBiexzpWLcKkVQI5XWKv8NqdHBK2TSlc7gO4U6wbWnyrJa6u8kouHxV8jj7kg05jUSswPUH9SNLstK41LrZZrwfZsO7GM; _ym_uid=1619885137311910967; _ym_d=1619885137; _rdt_uuid=1619885145324.e22633d3-93c3-4f64-a789-a3c2bc2e688d; _fbp=fb.1.1619885153815.1134328420; _gcl_au=1.1.1898123549.1619885157; __gads=ID=f9aab0cd3e873164:T=1619893589:S=ALNI_MaXmx_5btIQI2K4Cl-KSEYyHmFLUw; _vid=vNGYKLznCfMrCtergCaq; DFID=web|vNGYKLznCfMrCtergCaq; bc.visitor_token=6794946082859483136; _cs_c=1; omSeen-tgjg3ieouzbhy6fc0ctw=1620051477539; gidr=MA; sbm_dma=0; sbm_country=RS; _sctr=1|1621458000000; al_cell=2021-5-20-wt-main-1-control; chgcsdetaintoken=1; chgcsastoken=JAhZDkgz7vFDI1GpaiuEr0M0QVQDGclNfXjkKDyzeu20TYkiQ9WTJ1jQz2gYeoTRlj4I99G7ixdVIe8n1NKW5VEDwnTeh0z6UofMW9PT8oMiXyija-QUeb092GrnSbKP; adobeujs-optin=%7B%22aam%22%3Atrue%2C%22adcloud%22%3Atrue%2C%22aa%22%3Atrue%2C%22campaign%22%3Atrue%2C%22ecid%22%3Atrue%2C%22livefyre%22%3Atrue%2C%22target%22%3Atrue%2C%22mediaaa%22%3Atrue%2C%22videoaa%22%3Atrue%7D; _cs_id=187c707b-4c69-a726-cade-775cf9eb1c27.1620041470.3.1621528172.1621527423.1.1654205470758.Lax.0; __CT_Data=gpv=4&ckp=tld&dm=chegg.com&apv_79_www33=4&cpv_79_www33=4; PHPSESSID=d65a435d4867e05e9ceeee601b9dbad0; CSessionID=1c9de5ea-099d-406b-b331-22764d7d51f4; user_geo_location=%7B%22country_iso_code%22%3A%22IQ%22%2C%22country_name%22%3A%22Iraq%22%2C%22region%22%3A%22BG%22%2C%22region_full%22%3A%22Baghdad%22%2C%22city_name%22%3A%22Baghdad%22%2C%22locale%22%3A%7B%22localeCode%22%3A%5B%22ar-IQ%22%5D%7D%7D; AMCVS_3FE7CBC1556605A77F000101%40AdobeOrg=1; _gd1622237960795=1; CVID=29258665018562375872478304979529442280; sbm_a_b_test=1-control; CSID=1622237961382; mcid=29258665018562375872478304979529442280; schoolapi=null; _gid=GA1.2.1735757371.1622238036; chgmfatoken=%5B%20%22account_sharing_mfa%22%20%3D%3E%201%2C%20%22user_uuid%22%20%3D%3E%207edd9b9f-5206-4565-b447-cb17f4a7f524%2C%20%22created_date%22%20%3D%3E%202021-05-28T21%3A44%3A38.807Z%20%5D; _px3=25d9c98cc18282755832ae0c339030628c3665d6b1375b149543347e486a6197:QWlhjJm8LWF2ILg5r7XYOXngMqGeE15Uy1iEeWxJnAly4v4r3nWSiMPcwox+gJ5i4WW6pALQihBR6nkaCkRsJA==:1000:CV9GDPPzVi75sCrM34/DhNKtuNuYGOoOGviWo7+2QxMr+3VCgTadtZ8bqrj0A1pKqiaxoT5VMtDAEo0YkM41P81SEnHrWZI6snmVs8O6cnQRezY4hNOtP51/mhdE3fLOicdI9OP24vh2B9bsR/6Kk5Or2hutEoJF3VwdqfQ1Hc3fkSUPpObD+S48r27z/r4MkvLdKER38EZsKM7b5P6TCw==; id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI3ZWRkOWI5Zi01MjA2LTQ1NjUtYjQ0Ny1jYjE3ZjRhN2Y1MjQiLCJhdWQiOiJDSEdHIiwiaXNzIjoiaHViLmNoZWdnLmNvbSIsImV4cCI6MTYzODAwODM2OSwiaWF0IjoxNjIyMjM4MzY5LCJlbWFpbCI6ImFhc29hbmE3QGdtYWlsLmNvbSJ9.aTt87sSGIABh73qQzOGKnAZFHsqOA9pY8S9_3E0DHzgF4sW53IpDE4Z74o2GwTeuqhvpHtRBK4n5uNuowzK5W1BsyvLvbyIF3rZagMcgHHy-13QYTiq2trWM_DojKvG-YleQ18dHWasnIl5mDVJlSOMOt0mCyftOscPePQ6AtU_1HK6ElUq5_PWbrWRGibFdcCZ1oYV-d4NphAPW6UaDxqiVVpaS66RdEyP-_1fGCvk5MU9UM9Ev4RwPg9rUY7ecJbiIVzBU_XqCbBq-Ns83i7j7YrKbcWIIFGGew4UhCo_o5pQ9o1g5uy_NWk99dLOGwLdcRuS0lrt0d_y4RJEYQA; access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhUTkU0cWwxNTRxekZieTBBakxDdSJ9.eyJodHRwczovL3Byb3h5LmNoZWdnLmNvbS9jbGFpbXMvYXBwSWQiOiJOc1lLd0kwbEx1WEFBZDB6cVMwcWVqTlRVcDBvWXVYNiIsImlzcyI6Imh0dHBzOi8vY2hlZ2ctcHJvZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8N2VkZDliOWYtNTIwNi00NTY1LWI0NDctY2IxN2Y0YTdmNTI0IiwiYXVkIjpbImNoZWdnLW9pZGMiLCJodHRwczovL2NoZWdnLXByb2QudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMjIzODM2OSwiZXhwIjoxNjIyMjM5ODA5LCJhenAiOiIzVFpiaGZzWndkZUhiaG9WTXhPdlpHYjM3TWN2YzBvOCIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgYWRkcmVzcyBwaG9uZSBvZmZsaW5lX2FjY2VzcyIsImd0eSI6InBhc3N3b3JkIn0.L_rYE28yUT-oQdOro4axmqpuU34W-OpJQRoeFoVHcNGU15jgJk6ixngYC_-T67GPPeyZsOfEVPoUR7VxqGSnSbfwktksdM7Y7pNG5VK6DDd4VVfibbzshkAmu9DewDK_u9DQpQuYikNroIlbNbbuIszm6D6ib_Fu_o_doxgyTwIZ5s3OZ8FgqsvMtm24xiwlSc4bYVoWCY-amuDlNpvCDbow04MqEOM246Op4GBIuKYHj0XyQDrzY8ZZobkeFgVi7zIef-s9ulz2mZHlN7RfPl-OM9y0jRD3LQkGpOPPj3eACo9JQGSE9we-ZC5cnMAb-bug7KSaf-Srt4Clbpvxfw; access_token_expires_at=1622239809; refresh_token=ext.a0.t00.v1.MeKnVdKrC_Ew12IGfxIFlB8DyAWwI22BBREFLvgvmtBeiVzh1plRWGjg8holcAB6lTnhmj2cMBFlTgRQGtqGbSs; SU=p9468Wh5dH7_GHhNJas5tm0eJsXF12Nv2YfhET8etWepocuDA8SkvOu_koeaEc1MJwdyM-5tRX7_AtEFdI-A2hnZ3oQQuyjZS8KjssqlAbEzYeKYc0Q7njYFqp73bVE2; U=9f01cd4ecf7179f0c4b9f7311bd62dce; gid=1565637; exp=A311C%7CA803B%7CA100A%7CA184B%7CC024B%7CA560B%7CA259B%7CA207B%7CA209A%7CA212A%7CA890H%7CA448A%7CA270C%7CA966F%7CA278C%7CA935B; expkey=E19C2C144E76BC8754265777D8283DB8; intlPaQExitIntentModal=hide; _sdsat_cheggUserUUID=7edd9b9f-5206-4565-b447-cb17f4a7f524; _sdsat_authState=Hard%20Logged%20In; AMCV_3FE7CBC1556605A77F000101%40AdobeOrg=-408604571%7CMCIDTS%7C18776%7CMCMID%7C29258665018562375872478304979529442280%7CMCAAMLH-1622843208%7C6%7CMCAAMB-1622843208%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1622245608s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.6.0%7CMCCIDH%7C-215200707; chgcsdmtoken=%7B%22user_uuid%22%3A%227edd9b9f-5206-4565-b447-cb17f4a7f524%22%2C%22created_date%22%3A%222021-05-28T21%3A48%3A31.274Z%22%2C%22account_sharing_device_management%22%3A1%7D; OptanonConsent=isIABGlobal=false&datestamp=Sat+May+29+2021+00%3A50%3A01+GMT%2B0300+(%D8%A7%D9%84%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A+%D8%A7%D9%84%D8%B1%D8%B3%D9%85%D9%8A)&version=6.10.0&landingPath=NotLandingPage&groups=snc%3A1%2Cprf%3A1%2Cfnc%3A1%2Ctrg%3A1%2CSPD_BG%3A1&AwaitingReconsent=false&hosts=&consentId=8c64dfb3-587b-431c-9618-7b7ca08f7756&interactionCount=0; _px3=c8ee80636d66651a2e981b24fb52311c89cc161f1ed389403a77662c9372c0ea:Era4xKo2TIzWI6Vx6LZnzPSwMxrNZq08ukwQh1eIw3cFWf0l3tgl5ZCPuB1TcWv2GrGEhlTUK+kfGTwqZwRpNg==:1000:2TfQaQAy0YQvLb76GT6kxNVMRdA5Jme94gjk5fiF9WOPXxfXaWCPPT4PkgicFHpeLrsIGmvOAi1UNImpnQIKLWSInVmGC06lO0ebw6LmSoli6TQabCSIq5LzS05M2YeDLItXgyAQju7bqXJ6rw0J5t52PWxw7bvVRgIaa5/zcGiov2Qo9LB5DJX0HGSYfULqHjJob4bUSap6AKFm8j9g6g==; _px=Era4xKo2TIzWI6Vx6LZnzPSwMxrNZq08ukwQh1eIw3cFWf0l3tgl5ZCPuB1TcWv2GrGEhlTUK+kfGTwqZwRpNg==:1000:VVr/Ih2cxIXusju10OzGdzGwgqA83OsAMKAHZCda3kgfZbFQuazrJvno0342kHgWSaSMJLdD3dzlmXaiCn4h+jPhj505YHBuMWAG7ezYdkH3B1+HstClUfm0DIIFNM7dovuiKLPq/dwAvobg4bMKRmvDM+YGgVPtgxWLW5bbNKs9DnP/eODDSDh7trmxnrlcDEGOth4PBpLWTFQjLtJOWdyJSVJzxVl8EVbk6eNcrVaYpDkscig0rJBYB8qDbiaU74eeIyLMGuGdHxoexdROMA==; _uetsid=5b1656a0bffd11ebafc789ee45182185; _uetvid=1c70d0c0aa9711ebb3b16d960eeeb10c; _gat=1; wcs_bt=s_4544d378d9e5:1622238626; chgcsdmtoken=7edd9b9f-5206-4565-b447-cb17f4a7f524++web|vNGYKLznCfMrCtergCaq++1622238637469; s_pers=%20buFirstVisit%3Dstudy-pack%252Ccs%252Ccore%252Chelp%7C1779294569627%3B%20gpv_v6%3Dchegg%257Cweb%257Ccore%257Cmyaccount%257Cdevices%7C1622240439003%3B; s_sess=%20buVisited%3Dcs%252Ccore%3B%20s_ptc%3D0.01%255E%255E0.04%255E%255E0.00%255E%255E0.70%255E%255E7.06%255E%255E27.85%255E%255E600%255E%255E0.76%255E%255E600%3B%20cheggCTALink%3Dfalse%3B%20SDID%3D65808112A7BDA43B-4458250B3ED61F53%3B%20s_sq%3Dcheggincriovalidation%253D%252526pid%25253Dchegg%2525257Cweb%2525257Ccore%2525257Cmyaccount%2525257Cdevices%252526pidt%25253D1%252526oid%25253Dfunctionln%25252528%25252529%2525257B%2525257D%252526oidt%25253D2%252526ot%25253DSUBMIT%3B; _gali=redirect-on-remove-device-dialog; _pxff_cc=U2FtZVNpdGU9TGF4Ow==',
                    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                    'sec-ch-ua-mobile': '?0', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
                r = requests.get(url, headers=headers).content
                soup = BeautifulSoup(r, 'html.parser')
                x0 = soup.find('div', '</div>', class_="ugc-base question-body-text")
                x1 = soup.find('div', '</div>', class_="answer-given-body ugc-base")
                if x1 == None:
                    bot.reply_to(message, "عذرا عزيزي قم بفتح الرابط ثم قم بنسخه من اعلى المتصفح ومن ثم ارساله")
                else:
                    bot.reply_to(message, "♥ ♥  سيتم ارسال الاجابة في  غضون ثواني")
                    dds = sum([1 for i in x1.find_all('img') if '//d2vlcm61l7u1fs.cloudfront.net' in i['src']])
                    print(dds)
                    if dds==0:
                        rt = str(time.clock())
                        mma = rt.split(".")[0]
                        f = open("answer.html", "w", encoding='utf8')
                        mmes = """
                                                                                                                                                                <html>
                                                                                                                                                                <head>
                                                                                                                                                                <link href='http://fonts.googleapis.com/css?family=Droid+Sans' rel='stylesheet' type='text/css'>
                                                                                                                                                                <meta charset="utf-8"/>
                                                                                                                                                                <meta content="IE=11" http-equiv="X-UA-Compatible"/>
                                                                                                                                                                <meta content="width=device-width, initial-scale=1, maximum-scale=10" name="viewport"/>
                                                                                                                                                                </head>
                                                                                                                                                                <style> .hi{{background-color: #FFC133; width:800px; border-radius:6px;


                                                                                                                                                                }}
                                                                                                                                    .us{{background-color: #05ABD5;width:100%; width:800px; border-radius:6px;}}

                                                                                                                                    h3{{
                                                                                                                                        color: white;
                                                                                                                                        font-family: 'Droid Sans', arial, serif;;
                                                                                                                                        text-align: center;
                                                                                                                                        font-size:22px;
                                                                                                                                    }}
                                                                                                                                    h2{{
                                                                                                                                        color: #302F2D;
                                                                                                                                        font-family: 'Droid Sans', arial, serif;;
                                                                                                                                        text-align: center;
                                                                                                                                        font-size:22px;
                                                                                                                                    }}
                                                                                                                                    h4{{text-align:center; color:white; font-size:30px; font-family: 'Droid Sans', arial, serif;;}}
                                                                                                                                    .qa{{border:13px solid #FFC133; font-size:20px; width:800px;}}
                                                                                                                                    .q1{{background-color:#D50524; border-radius:6px; width:800px;}}
                                                                                                                                    .q2{{background-color:#05D52D; border-radius:6px; width:800px;}}
                                                                                                                                    </style>
                                                                                                                                        <body> <div class="hi">
                                                                                                                                        <h2>By Eng Mahmoud Fadhil</h2>
                                                                                                                                        </div> <div class="us">
                                                                                                                                        <h3>Follow us on Telegram @eng2028 and @Chegg_1</h3>
                                                                                                                                        </div><div class="q1"><h4>Question</h4></div><div class="qa" align="center">{Q}</div><div class="q2"><h4>Answer</h4></div><div class="qa" align="center">{A}</div></body>
                                                                                                                                                                </html>
                                                                                                                                                                """.format(
                            Q=x0, A=x1)

                        f.write(mmes)
                        f.close()
                        i = open('./answer.html', 'rb')
                        try:
                            bot.send_document(message.chat.id, i,
                                              caption="🌐 Answer\n\n🛡 Join Channel : @eng2080\n\n🛑 Contact : @eng2028\n\n @Qissm22 \n\n ⏱ Time : " + str(
                                                  mma) + 's', parse_mode="Markdown",
                                              disable_notification=True, reply_to_message_id=message.message_id)
                        except:
                            pass

                    if dds == 1:
                        s = x1.findAll('img')[0]['src']
                        bbz = s.split("//")[1]
                        jj = f"https://{bbz}?x-oss-process=image/resize,w_560"
                        g = str(x1).replace(s, jj)
                        rt = str(time.clock())
                        mma = rt.split(".")[0]
                        f = open("answer.html", "w", encoding='utf8')
                        mmes = """
                                                                                                                                        <html>
                                                                                                                                        <head>
                                                                                                                                        <link href='http://fonts.googleapis.com/css?family=Droid+Sans' rel='stylesheet' type='text/css'>
                                                                                                                                        <meta charset="utf-8"/>
                                                                                                                                        <meta content="IE=11" http-equiv="X-UA-Compatible"/>
                                                                                                                                        <meta content="width=device-width, initial-scale=1, maximum-scale=10" name="viewport"/>
                                                                                                                                        </head>
                                                                                                                                        <style> .hi{{background-color: #FFC133; width:800px; border-radius:6px;


                                                                                                                                        }}
                                                                                                            .us{{background-color: #05ABD5;width:100%; width:800px; border-radius:6px;}}

                                                                                                            h3{{
                                                                                                                color: white;
                                                                                                                font-family: 'Droid Sans', arial, serif;;
                                                                                                                text-align: center;
                                                                                                                font-size:22px;
                                                                                                            }}
                                                                                                            h2{{
                                                                                                                color: #302F2D;
                                                                                                                font-family: 'Droid Sans', arial, serif;;
                                                                                                                text-align: center;
                                                                                                                font-size:22px;
                                                                                                            }}
                                                                                                            h4{{text-align:center; color:white; font-size:30px; font-family: 'Droid Sans', arial, serif;;}}
                                                                                                            .qa{{border:13px solid #FFC133; font-size:20px; width:800px;}}
                                                                                                            .q1{{background-color:#D50524; border-radius:6px; width:800px;}}
                                                                                                            .q2{{background-color:#05D52D; border-radius:6px; width:800px;}}
                                                                                                            </style>
                                                                                                                <body> <div class="hi">
                                                                                                                <h2>By Eng Mahmoud Fadhil</h2>
                                                                                                                </div> <div class="us">
                                                                                                                <h3>Follow us on Telegram @eng2028 and @Chegg_1</h3>
                                                                                                                </div><div class="q1"><h4>Question</h4></div><div class="qa" align="center">{Q}</div><div class="q2"><h4>Answer</h4></div><div class="qa" align="center">{A}</div></body>
                                                                                                                                        </html>
                                                                                                                                        """.format(
                            Q=x0, A=g)

                        f.write(mmes)
                        f.close()
                        i = open('./answer.html', 'rb')
                        try:
                            bot.send_document(message.chat.id, i,
                                              caption="🌐 Answer\n\n🛡 Join Channel : @eng2080\n\n🛑 Contact : @eng2028\n\n  @Qissm22 \n\n ⏱ Time : " + str(
                                                  mma) + 's', parse_mode="Markdown",
                                              disable_notification=True, reply_to_message_id=message.message_id)
                        except:
                            pass
                    elif dds == 2:
                        s = x1.findAll('img')[0]['src']
                        dd = x1.findAll('img')[1]['src']
                        bbz = s.split("//")[1]
                        kkm = dd.split("//")[1]
                        jj = f"https://{bbz}?x-oss-process=image/resize,w_560"
                        cc = f"https://{kkm}?x-oss-process=image/resize,w_560"
                        g = str(x1).replace(s, jj).replace(dd, cc)
                        rt = str(time.clock())
                        mma = rt.split(".")[0]
                        f = open("answer.html", "w", encoding='utf8')
                        mmes = """
                                                                                                                                                                    <html>
                                                                                                                                                                    <head>
                                                                                                                                                                    <link href='http://fonts.googleapis.com/css?family=Droid+Sans' rel='stylesheet' type='text/css'>
                                                                                                                                                                    <meta charset="utf-8"/>
                                                                                                                                                                    <meta content="IE=11" http-equiv="X-UA-Compatible"/>
                                                                                                                                                                    <meta content="width=device-width, initial-scale=1, maximum-scale=10" name="viewport"/>
                                                                                                                                                                    </head>
                                                                                                                                                                    <style> .hi{{background-color: #FFC133; width:800px; border-radius:6px;


                                                                                                                                                                    }}
                                                                                                                                        .us{{background-color: #05ABD5;width:100%; width:800px; border-radius:6px;}}

                                                                                                                                        h3{{
                                                                                                                                            color: white;
                                                                                                                                            font-family: 'Droid Sans', arial, serif;;
                                                                                                                                            text-align: center;
                                                                                                                                            font-size:22px;
                                                                                                                                        }}
                                                                                                                                        h2{{
                                                                                                                                            color: #302F2D;
                                                                                                                                            font-family: 'Droid Sans', arial, serif;;
                                                                                                                                            text-align: center;
                                                                                                                                            font-size:22px;
                                                                                                                                        }}
                                                                                                                                        h4{{text-align:center; color:white; font-size:30px; font-family: 'Droid Sans', arial, serif;;}}
                                                                                                                                        .qa{{border:13px solid #FFC133; font-size:20px; width:800px;}}
                                                                                                                                        .q1{{background-color:#D50524; border-radius:6px; width:800px;}}
                                                                                                                                        .q2{{background-color:#05D52D; border-radius:6px; width:800px;}}
                                                                                                                                        </style>
                                                                                                                                            <body> <div class="hi">
                                                                                                                                            <h2>By Eng Mahmoud Fadhil</h2>
                                                                                                                                            </div> <div class="us">
                                                                                                                                            <h3>Follow us on Telegram @eng2028 and @Chegg_1</h3>
                                                                                                                                            </div><div class="q1"><h4>Question</h4></div><div class="qa" align="center">{Q}</div><div class="q2"><h4>Answer</h4></div><div class="qa" align="center">{A}</div></body>
                                                                                                                                                                    </html>
                                                                                                                                                                    """.format(
                            Q=x0, A=g)

                        f.write(mmes)
                        f.close()
                        i = open('./answer.html', 'rb')
                        try:
                            bot.send_document(message.chat.id, i,
                                              caption="🌐 Answer\n\n🛡 Join Channel : @eng2080\n\n🛑 Contact : @eng2028\n\n⏱ Time : " + str(
                                                  mma) + 's', parse_mode="Markdown",
                                              disable_notification=True, reply_to_message_id=message.message_id)
                        except:
                            pass
                    elif dds == 3:
                        s = x1.findAll('img')[0]['src']
                        dd = x1.findAll('img')[1]['src']
                        bn = x1.findAll('img')[2]['src']
                        bbz1 = s.split("//")[1]
                        bbz2 = dd.split("//")[1]
                        bbz3 = bn.split("//")[1]
                        jj = f"https://{bbz1}?x-oss-process=image/resize,w_560"
                        cc = f"https://{bbz2}?x-oss-process=image/resize,w_560"
                        ll = f"https://{bbz3}?x-oss-process=image/resize,w_560"
                        g = str(x1).replace(s, jj).replace(dd, cc).replace(bn, ll)
                        rt = str(time.clock())
                        mma = rt.split(".")[0]
                        f = open("answer.html", "w", encoding='utf8')
                        mmes = """
                                                                                                                                                                    <html>
                                                                                                                                                                    <head>
                                                                                                                                                                    <link href='http://fonts.googleapis.com/css?family=Droid+Sans' rel='stylesheet' type='text/css'>
                                                                                                                                                                    <meta charset="utf-8"/>
                                                                                                                                                                    <meta content="IE=11" http-equiv="X-UA-Compatible"/>
                                                                                                                                                                    <meta content="width=device-width, initial-scale=1, maximum-scale=10" name="viewport"/>
                                                                                                                                                                    </head>
                                                                                                                                                                    <style> .hi{{background-color: #FFC133; width:800px; border-radius:6px;


                                                                                                                                                                    }}
                                                                                                                                        .us{{background-color: #05ABD5;width:100%; width:800px; border-radius:6px;}}

                                                                                                                                        h3{{
                                                                                                                                            color: white;
                                                                                                                                            font-family: 'Droid Sans', arial, serif;;
                                                                                                                                            text-align: center;
                                                                                                                                            font-size:22px;
                                                                                                                                        }}
                                                                                                                                        h2{{
                                                                                                                                            color: #302F2D;
                                                                                                                                            font-family: 'Droid Sans', arial, serif;;
                                                                                                                                            text-align: center;
                                                                                                                                            font-size:22px;
                                                                                                                                        }}
                                                                                                                                        h4{{text-align:center; color:white; font-size:30px; font-family: 'Droid Sans', arial, serif;;}}
                                                                                                                                        .qa{{border:13px solid #FFC133; font-size:20px; width:800px;}}
                                                                                                                                        .q1{{background-color:#D50524; border-radius:6px; width:800px;}}
                                                                                                                                        .q2{{background-color:#05D52D; border-radius:6px; width:800px;}}
                                                                                                                                        </style>
                                                                                                                                            <body> <div class="hi">
                                                                                                                                            <h2>By Eng Mahmoud Fadhil</h2>
                                                                                                                                            </div> <div class="us">
                                                                                                                                            <h3>Follow us on Telegram @eng2028 and @Chegg_1</h3>
                                                                                                                                            </div><div class="q1"><h4>Question</h4></div><div class="qa" align="center">{Q}</div><div class="q2"><h4>Answer</h4></div><div class="qa" align="center">{A}</div></body>
                                                                                                                                                                    </html>
                                                                                                                                                                    """.format(
                            Q=x0, A=g)

                        f.write(mmes)
                        f.close()
                        i = open('./answer.html', 'rb')
                        try:
                            bot.send_document(message.chat.id, i,
                                              caption="🌐 Answer\n\n🛡 Join Channel : @eng2080\n\n🛑 Contact : @eng2028\n\n⏱ Time : " + str(
                                                  mma) + 's', parse_mode="Markdown",
                                              disable_notification=True, reply_to_message_id=message.message_id)
                        except:
                            pass
                    elif dds == 4:
                        s = x1.findAll('img')[0]['src']
                        dd = x1.findAll('img')[1]['src']
                        bn = x1.findAll('img')[2]['src']
                        bl = x1.findAll('img')[3]['src']
                        bbz1 = s.split("//")[1]
                        bbz2 = dd.split("//")[1]
                        bbz3 = bn.split("//")[1]
                        bbz4 = bl.split("//")[1]
                        jj = f"https://{bbz1}?x-oss-process=image/resize,w_560"
                        cc = f"https://{bbz2}?x-oss-process=image/resize,w_560"
                        ll = f"https://{bbz3}?x-oss-process=image/resize,w_560"
                        llx = f"https://{bbz4}?x-oss-process=image/resize,w_560"
                        g = str(x1).replace(s, jj).replace(dd, cc).replace(bn, ll).replace(bl, llx)
                        rt = str(time.clock())
                        mma = rt.split(".")[0]
                        f = open("answer.html", "w", encoding='utf8')
                        mmes = """
                                                                                                                                                                                                <html>
                                                                                                                                                                                                <head>
                                                                                                                                                                                                <link href='http://fonts.googleapis.com/css?family=Droid+Sans' rel='stylesheet' type='text/css'>
                                                                                                                                                                                                <meta charset="utf-8"/>
                                                                                                                                                                                                <meta content="IE=11" http-equiv="X-UA-Compatible"/>
                                                                                                                                                                                                <meta content="width=device-width, initial-scale=1, maximum-scale=10" name="viewport"/>
                                                                                                                                                                                                </head>
                                                                                                                                                                                                <style> .hi{{background-color: #FFC133; width:800px; border-radius:6px;


                                                                                                                                                                                                }}
                                                                                                                                                                    .us{{background-color: #05ABD5;width:100%; width:800px; border-radius:6px;}}

                                                                                                                                                                    h3{{
                                                                                                                                                                        color: white;
                                                                                                                                                                        font-family: 'Droid Sans', arial, serif;;
                                                                                                                                                                        text-align: center;
                                                                                                                                                                        font-size:22px;
                                                                                                                                                                    }}
                                                                                                                                                                    h2{{
                                                                                                                                                                        color: #302F2D;
                                                                                                                                                                        font-family: 'Droid Sans', arial, serif;;
                                                                                                                                                                        text-align: center;
                                                                                                                                                                        font-size:22px;
                                                                                                                                                                    }}
                                                                                                                                                                    h4{{text-align:center; color:white; font-size:30px; font-family: 'Droid Sans', arial, serif;;}}
                                                                                                                                                                    .qa{{border:13px solid #FFC133; font-size:20px; width:800px;}}
                                                                                                                                                                    .q1{{background-color:#D50524; border-radius:6px; width:800px;}}
                                                                                                                                                                    .q2{{background-color:#05D52D; border-radius:6px; width:800px;}}
                                                                                                                                                                    </style>
                                                                                                                                                                        <body> <div class="hi">
                                                                                                                                                                        <h2>By Eng Mahmoud Fadhil</h2>
                                                                                                                                                                        </div> <div class="us">
                                                                                                                                                                        <h3>Follow us on Telegram @eng2028 and @Chegg_1</h3>
                                                                                                                                                                        </div><div class="q1"><h4>Question</h4></div><div class="qa" align="center">{Q}</div><div class="q2"><h4>Answer</h4></div><div class="qa" align="center">{A}</div></body>
                                                                                                                                                                                                </html>
                                                                                                                                                                                                """.format(
                            Q=x0, A=g)

                        f.write(mmes)
                        f.close()
                        i = open('./answer.html', 'rb')
                        try:
                            bot.send_document(message.chat.id, i,
                                              caption="🌐 Answer\n\n🛡 Join Channel : @eng2080\n\n🛑 Contact : @eng2028\n\n @Qissm22 \n\n ⏱ Time : " + str(
                                                  mma) + 's', parse_mode="Markdown",
                                              disable_notification=True, reply_to_message_id=message.message_id)
                        except:
                            pass
                    elif dds == 5:
                        s = x1.findAll('img')[0]['src']
                        dd = x1.findAll('img')[1]['src']
                        bn = x1.findAll('img')[2]['src']
                        bl = x1.findAll('img')[3]['src']
                        bx = x1.findAll('img')[4]['src']
                        bbz1 = s.split("//")[1]
                        bbz2 = dd.split("//")[1]
                        bbz3 = bn.split("//")[1]
                        bbz4 = bl.split("//")[1]
                        bbz5 = bx.split("//")[1]
                        jj = f"https://{bbz1}?x-oss-process=image/resize,w_560"
                        cc = f"https://{bbz2}?x-oss-process=image/resize,w_560"
                        ll = f"https://{bbz3}?x-oss-process=image/resize,w_560"
                        llx = f"https://{bbz4}?x-oss-process=image/resize,w_560"
                        llm = f"https://{bbz5}?x-oss-process=image/resize,w_560"
                        g = str(x1).replace(s, jj).replace(dd, cc).replace(bn, ll).replace(bl, llx).replace(bx, llm)
                        sleep(2)
                        rt = str(time.clock())
                        mma = rt.split(".")[0]
                        f = open("answer.html", "w", encoding='utf8')
                        mmes = """
                                                                                                                                                                                                <html>
                                                                                                                                                                                                <head>
                                                                                                                                                                                                <link href='http://fonts.googleapis.com/css?family=Droid+Sans' rel='stylesheet' type='text/css'>
                                                                                                                                                                                                <meta charset="utf-8"/>
                                                                                                                                                                                                <meta content="IE=11" http-equiv="X-UA-Compatible"/>
                                                                                                                                                                                                <meta content="width=device-width, initial-scale=1, maximum-scale=10" name="viewport"/>
                                                                                                                                                                                                </head>
                                                                                                                                                                                                <style> .hi{{background-color: #FFC133; width:800px; border-radius:6px;


                                                                                                                                                                                                }}
                                                                                                                                                                    .us{{background-color: #05ABD5;width:100%; width:800px; border-radius:6px;}}

                                                                                                                                                                    h3{{
                                                                                                                                                                        color: white;
                                                                                                                                                                        font-family: 'Droid Sans', arial, serif;;
                                                                                                                                                                        text-align: center;
                                                                                                                                                                        font-size:22px;
                                                                                                                                                                    }}
                                                                                                                                                                    h2{{
                                                                                                                                                                        color: #302F2D;
                                                                                                                                                                        font-family: 'Droid Sans', arial, serif;;
                                                                                                                                                                        text-align: center;
                                                                                                                                                                        font-size:22px;
                                                                                                                                                                    }}
                                                                                                                                                                    h4{{text-align:center; color:white; font-size:30px; font-family: 'Droid Sans', arial, serif;;}}
                                                                                                                                                                    .qa{{border:13px solid #FFC133; font-size:20px; width:800px;}}
                                                                                                                                                                    .q1{{background-color:#D50524; border-radius:6px; width:800px;}}
                                                                                                                                                                    .q2{{background-color:#05D52D; border-radius:6px; width:800px;}}
                                                                                                                                                                    </style>
                                                                                                                                                                        <body> <div class="hi">
                                                                                                                                                                        <h2>By Eng Mahmoud Fadhil</h2>
                                                                                                                                                                        </div> <div class="us">
                                                                                                                                                                        <h3>Follow us on Telegram @eng2028 and @Chegg_1</h3>
                                                                                                                                                                        </div><div class="q1"><h4>Question</h4></div><div class="qa" align="center">{Q}</div><div class="q2"><h4>Answer</h4></div><div class="qa" align="center">{A}</div></body>
                                                                                                                                                                                                </html>
                                                                                                                                                                                                """.format(
                            Q=x0, A=g)

                        f.write(mmes)
                        f.close()
                        i = open('./answer.html', 'rb')
                        try:
                            bot.send_document(message.chat.id, i,
                                              caption="🌐 Answer\n\n🛡 Join Channel : @eng2080\n\n🛑 Contact : @eng2028\n\n @Qissm22 \n\n ⏱ Time : " + str(
                                                  mma) + 's', parse_mode="Markdown",
                                              disable_notification=True, reply_to_message_id=message.message_id)
                        except:
                            pass
        else:
            pass


bot.polling()
