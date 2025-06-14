````markdown
# S3 Encryption Monitor using AWS Lambda and Boto3

## Objective

This project uses an AWS Lambda function to scan all S3 buckets in an AWS account and identify buckets that do not have server-side encryption (SSE) enabled.

## Files

- `lambda_function.py` – Python script to detect unencrypted S3 buckets.
- `README.md` – Project documentation.

## How It Works

1. The Lambda function lists all S3 buckets in the account.
2. It checks each bucket for server-side encryption.
3. Unencrypted bucket names are printed to the logs.

## Requirements

- Python 3.x (Lambda runtime)
- IAM Role with the following permissions:
  - `AmazonS3ReadOnlyAccess`
  - `AWSLambdaBasicExecutionRole`

## How to Use

1. Create a few S3 buckets. Enable encryption on some, leave others unencrypted.
2. Deploy this code as a Lambda function.
3. Assign the IAM role.
4. Manually trigger the function.
5. Check CloudWatch logs for results.

## Sample Output

```json
{
  "statusCode": 200,
  "unencrypted_buckets": ["my-unencrypted-bucket-1", "my-unencrypted-bucket-2"]
}
````

## Author

Vignesh Sadanki
[GitHub Profile](https://github.com/Sadanki)


```
