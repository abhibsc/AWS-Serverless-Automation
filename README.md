# Serverless AWS EC2 Automation

## Project Overview
This project automates EC2 instance start and stop
operations using AWS Lambda and Amazon CloudWatch.

## AWS Services Used
- AWS Lambda
- Amazon EC2
- Amazon CloudWatch
- AWS IAM

## Programming Language
- Python

## Features
- Automated EC2 start and stop operations.
- Serverless automation using AWS Lambda.
- Scheduled execution using Amazon CloudWatch.
- IAM permissions for secure AWS access.

## How It Works
1. Amazon CloudWatch triggers the Lambda function
   according to a configured schedule.
2. AWS Lambda executes the Python code.
3. The function sends a start or stop request to EC2.
4. CloudWatch logs help monitor execution.

## Files
- lambda_function.py: Python Lambda function.

## Security
AWS credentials should never be stored directly
in the source code.

## Author
Abhi M