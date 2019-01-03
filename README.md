# ceph-rgw


**FIRST** to prepare environment

**creating  user【eg. user=app.ceph】**
```
    radosgw-admin user create --uid=app.ceph --display-name=app.ceph
    radosgw-admin caps add --uid=app.ceph --caps="users=read, write"
    radosgw-admin caps add --uid=app.ceph --caps="usage=read, write"
````

**setting  placement**
```
    radosgw-admin metadata get user:app.ceph  > user.md.json
    EDIT user.md.json AND add app-placement to default-placement
    radosgw-admin metadata put user:app.ceph <user.md.json
```

**updating  zone**
```
    radosgw-admin zone get --rgw-zone=default > zone.json
    EDIT zone.json AND add describe info of placement
    radosgw-admin zone set --rgw-zone=default --infile zone.json
```

**add zone to zonegroup again**
```
    radosgw-admin zonegroup add --rgw-zonegroup=default --rgw-zone=default
```


**AFTER** above, you have  
(1) key of user=app.ceph  
- access_key  
- secret_key

(2) data placement for app.ceph    
this means, all write data for app.ceph will be save into app-placement(it have corresponding pools) 


**THEN** , exec bucket create script to CREATE bucket  

**LAST** use put or get to upload and download your object  



**NOTICE**  
authrozation of put is public-read(all id or user can read your object), if wanna use acl, choose put-acl.sh and take care of below lines in file

stringToSign="PUT\n\n\n${dateValue}\nx-amz-grant-read:**id=grantee.ceph**\n${resource}"

MUST the same as 

 -H "x-amz-grant-read: **id=grantee.ceph**" \

