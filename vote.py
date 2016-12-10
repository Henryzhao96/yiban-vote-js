import requests,random,pprint

fo = open('result.txt','w')
fi = open('tokens.txt','r')

def postdata(token, votedata):
    url = 'http://q.yiban.cn/vote/insertBoxAjax'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'http://q.yiban.cn',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'DNT': '1',
        'Referer': 'http://q.yiban.cn/app/index/appid/82055',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,ja;q=0.2',
        'Cookie': 'yiban_user_token='+token
        }

    payload = {
        'App_id': '82055',
        'VoteOption_id[]': votedata,
        'Vote_id': '10771'
        }

    r = requests.post(url, data=payload, headers=headers)
    resp=r.json()
    print(token+","+str(resp['code'])+","+resp['message'])
    fo.write(token+","+str(resp['code'])+","+resp['message']+"\n")
    fo.flush()
    return resp['code']



for line in fi:
    token = line[:-1]
    
    votetmp1=[372637,372641,372643,372653,372659,372661,372663,372665,372667,372669,372671,372675,372677,372679,372681,372687,372689,372693,372697,372701,372705,372709,372779,372783,372785,372851,372853,372857,372859,372863,372865,372877]
    votetmp2=[373211,373215,373221,373251,373253,373255,373259,373263,373265,373279,373283,373293,373295,373369,373373,373375,373379,373381,373383,373385]
    votetmp3=[371595,371603,371619,371693,371715,371723,372095,372099,372167,372233,372235,372237,372369,372437,372439,372441,372443,372445,372447,372449,372451,372519,372521,372523,372525,372527,372529,372531,372533,372535,372537,372539,372545,372547,372551,372553,372555,372557,372559,372561,372563,373505]
    votetmp4=[372979,372975,372981,372987,373065,373193,372973,373103,372995,373067,373091,373111,373115,373095,373113,373107,373099,373117,373109,373087,373121,373083,373125,373101,373089,373081,373119,373191]
    votetmp5=[373489,373393,373481,373411,373391,373415,373485,373395,373407,373499,373503,373495,373401,373399,373409,373491,373493]
    
    votedata = []
    tmpdata = random.sample(votetmp1,5)
    for i in tmpdata:
        votetmp1.remove(i)
    votedata.extend(tmpdata)
    votedata.extend([373387,372971,372435,372657,372991])
    if(postdata(token,votedata)==211):continue
    
    votedata = []
    tmpdata = random.sample(votetmp2,5)
    for i in tmpdata:
        votetmp2.remove(i)
    votedata.extend(tmpdata)
    votedata.extend([373387,372971,372435,372657,372991])
    postdata(token,votedata)
    
    votedata = []
    tmpdata = random.sample(votetmp3,5)
    for i in tmpdata:
        votetmp3.remove(i)
    votedata.extend(tmpdata)
    votedata.extend([373387,372971,372435,372657,372991])
    postdata(token,votedata)
    
    unuseddata = votetmp1 + votetmp2 + votetmp3
    
    votedata = []
    tmpdata = random.sample(votetmp4,1)
    votedata.extend(tmpdata)
    tmpdata = random.sample(unuseddata,4)
    for i in tmpdata:
        unuseddata.remove(i)
    votedata.extend(tmpdata)
    votedata.extend([373387,372971,372435,372657,372991])
    postdata(token,votedata)
    
    votedata = []
    tmpdata = random.sample(votetmp5,1)
    votedata.extend(tmpdata)
    tmpdata = random.sample(unuseddata,4)
    for i in tmpdata:
        unuseddata.remove(i)
    votedata.extend(tmpdata)
    votedata.extend([373387,372971,372435,372657,372991])
    postdata(token,votedata)
fi.close()
fo.close()
