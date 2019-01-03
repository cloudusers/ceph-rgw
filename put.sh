host="10.11.12.13:7480"
bucket="bucket-test"

file="/home/cepher/upload-test.log"
objname="myobject1"

resource="/${bucket}/${objname}"  
dateValue=`date -R -u`
stringToSign="PUT\n\n\n${dateValue}\n${resource}"  

s3Key="UQFLDM3RHGSDYB2VSZ9E"
s3Secret="6OLl8xyT1SajTSgPNUKNHCGSEWhjpEfEPpdXzs8i"

signature=`echo -en ${stringToSign} | openssl sha1 -hmac ${s3Secret} -binary | base64`  
echo $signature


curl -v -X PUT -T "${file}" \
  -H "Authorization: AWS ${s3Key}:${signature}" \
  -H "Host: ${host}" \
  -H "Date: ${dateValue}" \
  "${host}${resource}"
