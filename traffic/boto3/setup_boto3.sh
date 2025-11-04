#!/bin/bash

ROLE_ARN="arn:aws:iam::042844421190:role/S3WriterRole"
PROFILE="oscar-admin"
SESSION_NAME="s3-simulation"
REGION="us-east-2"

creds=$(aws sts assume-role --role-arn "$ROLE_ARN" --role-session-name "$SESSION_NAME" --profile "$PROFILE" --region "$REGION" --output json)

AWS_ACCESS_KEY_ID=$(echo "$creds" | jq -r '.Credentials.AccessKeyId')
AWS_SECRET_ACCESS_KEY=$(echo "$creds" | jq -r '.Credentials.SecretAccessKey')
AWS_SESSION_TOKEN=$(echo "$creds" | jq -r '.Credentials.SessionToken')
EXPIRATION=$(echo "$creds" | jq -r '.Credentials.Expiration')

export AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN AWS_REGION="$REGION"

echo Access Key: $AWS_ACCESS_KEY_ID
echo Secret Key: $AWS_SECRET_ACCESS_KEY
echo Session Token: $AWS_SESSION_TOKEN
