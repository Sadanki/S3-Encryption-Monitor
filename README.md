Here is your complete `README.md` file content — copy and paste this into your `S3-Encryption-Monitor` project folder in VS Code as `README.md`:

---

````markdown
# 🛡️ S3 Encryption Monitor using AWS Lambda and Boto3

## 🎯 Objective

To enhance AWS security posture by using a Lambda function that detects S3 buckets without server-side encryption (SSE).

---

## 🔧 What This Project Does

This AWS Lambda function:
- 🔍 Scans all S3 buckets in the account
- ❌ Identifies buckets without SSE
- ✅ Logs encrypted buckets
- 📜 Prints results to CloudWatch logs

---

## 📂 Files

- `lambda_function.py` – Python code for the Lambda function
- `README.md` – Project explanation and setup instructions

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

## 🛠️ How to Use

1. Create a few S3 buckets. Enable SSE for some, leave others unencrypted.
2. Create a Lambda function using Python 3.x.
3. Assign the IAM role with:

   * `AmazonS3ReadOnlyAccess`
   * `AWSLambdaBasicExecutionRole`
4. Paste the above code into the function.
5. Manually invoke and check CloudWatch logs.

---

## ✅ Sample Output

```json
{
  "statusCode": 200,
  "unencrypted_buckets": ["my-unencrypted-bucket-1", "my-unencrypted-bucket-2"]
}
```

---

## ✅ Benefits

| Feature              | Description                      |
| -------------------- | -------------------------------- |
| 🔒 Improves Security | Detects buckets without SSE      |
| 📊 Logs for Auditing | Output goes to CloudWatch        |
| 🤖 Automation Ready  | Can be scheduled via EventBridge |
| 📉 Cost Effective    | No infra to manage – serverless  |

---

## ⚠️ Limitations

* Does not enable encryption automatically
* Does not scan individual object encryption
* Works only in current AWS region context

---

## 🧠 Author

**Vignesh Sadanki**
GitHub: [@Sadanki](https://github.com/Sadanki)

```

---

Let me know when you're ready to add this to Git and push it, or if you'd like help creating similar `README.md` files for your other AWS Lambda assignments.
```
