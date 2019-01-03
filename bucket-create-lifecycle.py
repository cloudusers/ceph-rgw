import boto.s3.connection
from boto.s3.lifecycle import Lifecycle, Transitions, Rule, Expiration

bucket_name = 'exp-bucket-test'
bucket_acl  = 'public-read'

access_key = 'UQFLDM3RHGSDYB2VSZ9E'
secret_key = '6OLl8xyT1SajTSgPNUKNHCGSEWhjpEfEPpdXzs8i'

conn = boto.connect_s3(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        host='10.11.12.13', port=7480,
        is_secure=False, calling_format=boto.s3.connection.OrdinaryCallingFormat(),
       )

#Create
def create_bucket():
    conn.create_bucket(bucket_name)
    bucket = conn.get_bucket(bucket_name)
    ret = bucket.set_acl(bucket_acl)
    ret = bucket.get_acl()
    print "Bucket ACL:",ret

#LifeCycle
def lifecycle():
    #transitions = Transitions()
    exp= Expiration(date="2018-06-13 07:05:00")
    #exp = Expiration(days=1)
    rule = Rule(id='rule-1', prefix='', status='Enabled', expiration=exp)
    lifecycle = Lifecycle()
    lifecycle.append(rule)

    bucket = conn.get_bucket(bucket_name)
    ret = bucket.configure_lifecycle(lifecycle)
    print "Bucket Lifecycle Set:",ret
    print "========================="
    
    
    current = bucket.get_lifecycle_config()
    print "Bucket Lifecycle Conf:", current
    print "Tran:", current[0].transition
    print "Expi:", current[0].expiration
    print "========================="

#Expire
def expire_key():
    bucket = conn.get_bucket(bucket_name)
    key = bucket.get_key("myobject108")
    #print key.expiry_date
    print "Bucket->key.expire:", key
    print "========================="

if __name__=='__main__':
    create_bucket()
    lifecycle()
    expire_key()

    print "right?"
