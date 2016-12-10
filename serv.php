<?php
/**
 * Created by PhpStorm.
 * User: shzha
 * Date: 2016/11/22
 * Time: 4:41
 */
$appid=69093; //appid to follow

function encrypt($sData, $sKey){
    $sResult = '';
    for($i=0;$i<strlen($sData);$i++){
        $sChar    = substr($sData, $i, 1);
        $sKeyChar = substr($sKey, ($i % strlen($sKey)) - 1, 1);
        $sChar    = chr(ord($sChar) + ord($sKeyChar));
        $sResult .= $sChar;
    }
    return encode_base64($sResult);
}
function decrypt($sData, $sKey){
    $sResult = '';
    $sData   = decode_base64($sData);
    for($i=0;$i<strlen($sData);$i++){
        $sChar    = substr($sData, $i, 1);
        $sKeyChar = substr($sKey, ($i % strlen($sKey)) - 1, 1);
        $sChar    = chr(ord($sChar) - ord($sKeyChar));
        $sResult .= $sChar;
    }
    return $sResult;
}
function encode_base64($sData){
    $sBase64 = base64_encode($sData);
    return strtr($sBase64, '+/', '-_');
}
function decode_base64($sData){
    $sBase64 = strtr($sData, '-_', '+/');
    return base64_decode($sBase64);
}

date_default_timezone_set("Asia/Shanghai");
if(!isset($_GET['d'])) {
    exit(0);
}

$data=base64_decode(decrypt(str_replace('-','+',$_GET['d']),'UTuWvUgv69BHPcyb'));
//echo $data;


$json = json_decode($data,true);

$ssid = $json['ssid'];
$token = $json['token'];
$id = $json['appid'];
$vote = $json['vote'];

$f = fopen('statfornow233.txt','a');
fwrite($f,date("Y-m-d H:i:s").','.$id.','.$ssid.','.$token.','.$vote.','.$_SERVER['REMOTE_ADDR']."\r\n");
/*
$url = 'http://app.yiban.cn/ajax/visitapp';
$fields = array(
    'app_id' => $appid,
    'act' => 'add',
    'position' => '2-1'
);

//url-ify the data for the POST
foreach($fields as $key=>$value) { $fields_string .= $key.'='.$value.'&'; }
rtrim($fields_string, '&');

//open connection
$ch = curl_init();

//set the url, number of POST vars, POST data
curl_setopt($ch,CURLOPT_URL, $url);
curl_setopt($ch,CURLOPT_POST, count($fields));
curl_setopt($ch,CURLOPT_POSTFIELDS, $fields_string);
curl_setopt($ch,CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch,CURLOPT_HTTPHEADER, array(
    'Origin: http://app.yiban.cn',
    'Referer: http://app.yiban.cn/apps/search',
    'Cookie: YB_SSID='.$ssid.'; yiban_user_token='.$token.';',
    'User-Agent: '.$_SERVER['HTTP_USER_AGENT'],
	'X-Forwarded-For: '.$_SERVER['REMOTE_ADDR']
));

//execute post
$dt = curl_exec($ch);

//close connection
curl_close($ch);
*/
//$dt = json_decode($result, true);