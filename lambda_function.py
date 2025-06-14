import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    unencrypted_buckets = []

    # List all buckets
    response = s3.list_buckets()

    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        try:
            encryption = s3.get_bucket_encryption(Bucket=bucket_name)
            rules = encryption['ServerSideEncryptionConfiguration']['Rules']
            print(f"✅ {bucket_name} is encrypted with: {rules[0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']}")
        except s3.exceptions.ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'ServerSideEncryptionConfigurationNotFoundError':
                print(f"❌ {bucket_name} is NOT encrypted")
                unencrypted_buckets.append(bucket_name)
            else:
                print(f"⚠️ Error checking {bucket_name}: {str(e)}")

    print("📝 Unencrypted Buckets:", unencrypted_buckets)

    return {
        'statusCode': 200,
        'unencrypted_buckets': unencrypted_buckets
    }
