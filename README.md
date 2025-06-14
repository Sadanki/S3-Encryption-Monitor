Great! Since you've already created the repo:
🔗 [https://github.com/Sadanki/S3-Encryption-Monitor](https://github.com/Sadanki/S3-Encryption-Monitor)

Here’s exactly what you need:

---

## ✅ Final Git Commands (Run from VS Code Terminal)

Assuming you're in your local folder `S3-Encryption-Monitor`:

```bash
# Step 1: Initialize git repo
git init

# Step 2: Add all files (lambda_function.py + README.md)
git add .

# Step 3: Commit the changes
git commit -m "Initial commit: Lambda function to detect unencrypted S3 buckets"

# Step 4: Link your local repo to GitHub repo
git remote add origin https://github.com/Sadanki/S3-Encryption-Monitor.git

# Step 5: Set branch name to main
git branch -M main

# Step 6: Push to GitHub
git push -u origin main
```

---

## 📄 README.md (Copy and Paste in VS Code)

Create a file named `README.md` in the same folder and paste this:

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
4. Paste the above code.
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

Once you:
- Create `lambda_function.py`  
- Paste above into `README.md`  
- Run the git commands I shared

…your repo will look perfect on GitHub ✅

Let me know if you want me to package this as a zip too.
```
