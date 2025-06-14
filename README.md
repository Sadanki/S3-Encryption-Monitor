---

### ✅ `README.md` (Final Version)

````markdown
# 🛡️ S3 Encryption Monitor using AWS Lambda and Boto3

## 🎯 Objective

To enhance AWS security posture by using an AWS Lambda function that detects S3 buckets **without server-side encryption (SSE)** enabled.

---

## 🔧 What This Project Does

This AWS Lambda function:
- 🔍 Scans all S3 buckets in the AWS account
- ❌ Identifies buckets that **do not have SSE enabled**
- ✅ Logs encryption details for secure buckets
- 📜 Outputs results to **CloudWatch Logs**

---

## 📂 Files Included

- `lambda_function.py` – Python code for the Lambda function
- `README.md` – Documentation for the assignment

---

## 🪄 Lambda Function Code (Python 3.x)

```python
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    unencrypted_buckets = []

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
````

---

## 🚀 How to Use

1. ✅ **Create test S3 buckets**

   * Enable SSE on some buckets
   * Leave others unencrypted for testing

2. ✅ **Create IAM Role** for Lambda

   * Attach these policies:

     * `AmazonS3ReadOnlyAccess`
     * `AWSLambdaBasicExecutionRole`

3. ✅ **Create a Lambda Function**

   * Runtime: **Python 3.x**
   * Use the above code

4. ✅ **Test it manually**

   * Trigger the function
   * Check CloudWatch logs

---

## 🧪 Sample Output

```json
{
  "statusCode": 200,
  "unencrypted_buckets": ["my-unencrypted-bucket-1", "my-unencrypted-bucket-2"]
}
```

---

## ✅ Benefits

| Feature              | Description                               |
| -------------------- | ----------------------------------------- |
| 🔒 Improves Security | Detects misconfigured S3 buckets          |
| 📊 Auditable         | Results are logged in CloudWatch          |
| 🤖 Automation Ready  | Can be scheduled via EventBridge/Cron     |
| 💸 Cost-Effective    | Serverless & lightweight, no infra needed |

---

## ⚠️ Limitations

* Does **not auto-enable** encryption
* Only checks **bucket-level** encryption (not per-object)
* Limited to current AWS account & region

---

## 🧠 Author

**Vignesh Sadanki**
GitHub: [@Sadanki](https://github.com/Sadanki)

````


