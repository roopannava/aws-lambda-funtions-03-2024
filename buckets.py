import boto3

def number_buckets(num):
    client = boto3.client('s3')
    buckets = client.list_buckets()
    count = 0
    for bucket in buckets:
        print(f"processing buckt: {count}")
        if count < num:
            current_bucket = buckets['Buckets'][count]
            print(f"Fount bucket : {current_bucket}")
            
        count +=1    
number_buckets(1)