import csv
import urllib.request
import re
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
	#'Cookie':'bev=1592201118_NDE0NDE0MjU2MzYw; frmfctr=wide; cfrmfctr=DESKTOP; _pykey_=a91772d7-7b52-556f-9450-bb769cd56211; tzo=480; sdid=; ag_fid=sBslmx7jNppMwzBF; _gcl_au=1.1.20285352.1592201221; __ssid=508da33ca109724153ae11990d251ec; _ga=GA1.2.819246520.1592201231; _pt=1--WyI0YzFhOTZkZjBkYmI5OTQ4MWU0YjVkOTViYWFiODllNjQyZGUyMTM4Il0%3D--b3fca9e8011b07044474a7f571c16903dad9a66a; _aat=0%7CqHUBkmMehttXlU0wtUmIkeXm82rpWRSbZp6IS0dgk6dnn4vXNj2n3VPxM6z9SVHl; _airbed_session_id=2eff94b4fd6bf45d6e82dc143f0283f4; hli=1; _csrf_token=V4%24.airbnb.cn%24QYuxOciL0HE%24ReoXCpAcAqL33aFtrUARMlADLTNhAasJ64zrxHS_tTY%3D; jitney_client_session_id=7b75cbe5-5eee-49d7-9cfb-89188397ff1a; jitney_client_session_created_at=1594697213; flags=0; roles=0; __svt=470; currency=CNY; cbkp=4; jitney_client_session_updated_at=1594698802; _user_attributes=%7B%22curr%22%3A%22CNY%22%2C%22guest_exchange%22%3A6.999335%2C%22device_profiling_session_id%22%3A%221592201118--6c3e70761931d9d634bacdab%22%2C%22giftcard_profiling_session_id%22%3A%221594697214-350103365-22e0bde3903fd3b4d0f43bf6%22%2C%22reservation_profiling_session_id%22%3A%221594697214-350103365-b8f2ed069f89da3d8050603d%22%2C%22id%22%3A350103365%2C%22hash_user_id%22%3A%224c1a96df0dbb99481e4b5d95baab89e642de2138%22%2C%22eid%22%3A%22PEQtwSC9D1WMM4H9HdzO_Q%3D%3D%22%2C%22num_msg%22%3A0%2C%22num_notif%22%3A2%2C%22num_alert%22%3A3%2C%22num_h%22%3A0%2C%22num_trip_notif%22%3A0%2C%22name%22%3A%22%E3%80%82%22%2C%22num_action%22%3A0%2C%22is_admin%22%3Afalse%2C%22can_access_photography%22%3Afalse%2C%22travel_credit_status%22%3Anull%2C%22referrals_info%22%3A%7B%22receiver_max_savings%22%3A%22%EF%BF%A5553%22%2C%22receiver_savings_percent%22%3A0%2C%22receiver_signup%22%3A%22%EF%BF%A50%22%2C%22referrer_guest%22%3A%22%EF%BF%A575%22%2C%22terms_and_conditions_link%22%3A%22%2Fhelp%2Farticle%2F2269%22%2C%22wechat_link%22%3A%22https%3A%2F%2Fwww.airbnb.cn%2Fc%2F5272494%3Fcurrency%3DCNY%26s%3D11%22%2C%22offer_discount_type%22%3A%22tiered_savings%22%7D%7D',
	#'cookie': 'newsModal=true; loginModal=1; XSRF-TOKEN=eyJpdiI6IjA4MW11MVB0SGNmM1A1RThDNzVMdmc9PSIsInZhbHVlIjoiSTVDWlJrMjdCVHhMM0lGYlwvWU1Ma0REeXUzTk9PUVhIaGV4N2d6Q1kwYkE3ckMydE5USW8yVGg0azdIK1poRVQiLCJtYWMiOiI1YTVlZmY4ZjkzZjA4MWU5N2M0NmFiNDVhNWI0NmY4YWMwYjZjMjQ4MGFmNDdjNzYzOWMzM2E4YThjNDc2MWNkIn0%3D; cgli_session=eyJpdiI6Ikh4QlM4UGNqR21tRTcxTXNjSno2a2c9PSIsInZhbHVlIjoiUHhIdEgxWlhhbU9pUDJGVVY1dEdTMEJXM2FkZGphTkZ0V2tBZm5XS0h0VGkxd2UrUVRwd0JpbmtNZnZxUHcydyIsIm1hYyI6IjdhZTM1YjdhZWFlMjA1MmRmZjg5NWUwYjUzNTVmNjliN2NhOWVkN2FhNDM1YjE4MGMxYjA3MDFhNzFlNDk5Y2EifQ%3D%3D',
}
def spider_inner(url=r'https://www.metacritic.com/game/nintendo-64/the-legend-of-zelda-ocarina-of-time'):
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req).read().decode()
    try:
        rate_num=re.findall('<strong>(.*?) Ratings</strong>',response,re.S)[0]
    except:
        rate_num=''
    # print(rate_num)
    try:
        genre=re.findall('Genre\(s\): </span><span class="data" >(.*?)</span',response,re.S)[0]
    except:
        genre=''
    # print(genre)
    try:
        rating=re.findall('<span class="label">Rating:</span>.*?<span class="data" >(.*?)</span>',response,re.S)[0]
    except:
        rating=''
    # print(rating)
    return [rate_num,genre,rating]
    # with open('html.txt','w',encoding='utf-8') as writer:
    #     writer.write(response)

def spider():
    with open('data/game.csv', 'w', encoding='utf-8', newline='') as f:
        writer=csv.writer(f)
        header=['title','platform','date','summary','meta_socre','user_socre','rate_num','genre','rating']
        writer.writerow(header)
        for i in range(1,20):
            print('page:',i+1)
            url=r'https://www.metacritic.com/browse/games/score/metascore/all?page={}'.format(i)
            req=urllib.request.Request(url,headers=headers)
            response=urllib.request.urlopen(req).read().decode()
            # print(response)
            tr_res=re.findall("<tr>(.*?)</tr>",response,re.S)
            # print(len(tr_res),tr_res)
            for tr in tr_res:
                title=re.findall("<h3>(.*?)</h3>",tr,re.S)[0].replace('\n','')
                # print(title)
                platform=re.findall('<span class="data">(.*?)</span>',tr,re.S)[0].replace("  ",'').replace("\t",'').replace('\n','')
                # print(platform)
                date=re.findall("<span>(.*?)</span>",tr,re.S)[0]
                # print(date)
                summary=re.findall('<div class="summary">(.*?)</div>',tr,re.S)[0]
                # print(summary)
                meta_socre=re.findall('<div class="metascore_w large game .*?">(.*?)</div>',tr,re.S)[0]
                # print(meta_socre)
                user_socre=re.findall('<div class="metascore_w user large game .*?">(.*?)</div>',tr,re.S)[0]
                # print(user_socre)
                inner_url='https://www.metacritic.com/game/'+re.findall('<a href="/game/(.*?)"',tr,re.S)[0]
                try:
                    inner_res=spider_inner(inner_url)
                except:
                    inner_res=[]
                # print(inner_url)
                res=[title,platform,date,summary,meta_socre,user_socre]+inner_res
                print(len(res),res)
                writer.writerow(res)
                f.flush()
            # print(res)
    # with open('html.txt','w',encoding='utf-8') as writer:
    #     writer.write(response)

if __name__ == '__main__':
    spider()
    # spider_inner()