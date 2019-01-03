host="10.11.12.13:7480"
bucket="exp-bucket-test"

objname="myobject"

url="${host}"  
resource="/${bucket}/${objname}"  
dateValue=`date -R -u`  
#dateValue="Fri, 1 Jun 2018 04:55:27 GMTT"
stringToSign="GET\n\n\n${dateValue}\n${resource}"  
echo ${stringToSign}

s3Key="995HG73P56PM7A57780Q"
s3Secret="IUEQBJtH3wbx4qQEcqu0FegXvB1BpsWXj0a3HcKX"

signature=`echo -en ${stringToSign} | openssl sha1 -hmac ${s3Secret} -binary | base64`  
echo $signature
curl -v -X GET \
	-H "Authorization: AWS ${s3Key}:${signature}" \
	-H "Date: ${dateValue}" \
	-H "Host: ${host}" \
	"${host}${resource}"
