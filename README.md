## Introduction

This project deploys the backend for the Weekly Security Message Reminder Telegram Bot to AWS, using the Serverless Framework Component.

AWS Lambda is used for this project as it is low maintenance, scalable, and cheap for infrequent workloads (In this case, AWS offers 1 million requests free per month with the AWS Free Tier. The application will never charge for idle time, and require little-to-zero administration.

AWS Dynamo DB is chosen to store the states of the application. (AWS offers Dynamo DB with 25 GB of storage and up to 200 million read/write requests per month with the AWS Free Tier).

*_AWS Lambda is a serverless, event-driven compute service that lets you run code for virtually any type of application or backend service without provisioning or managing servers._

*_AWS Dynamo DB is a fast, flexible NoSQL database service for single-digit millisecond performance at any scale_

## Quick Start

### 1. Install

```bash
# Install Serverless Framework
npm install -g serverless
```

### 2. Deploy

You can use following command to deploy the APP. 

```bash
export TELEGRAM_TOKEN=123
export AWS_ACCESS_KEY_ID=123
export AWS_SECRET_ACCESS_KEY=123
serverless deploy
```

### 3. Monitor

Anytime you need to know more about your running express instance, you can run `serverless info` to view the most critical info. 
This is especially helpful when you want to know the outputs of your instances so that you can reference them in another instance. 
You will also see a url where you'll be able to view more info about your instance on the Serverless Dashboard.

It also shows you the status of your instance, when it was last deployed, and how many times it was deployed. 
To dig even deeper, you can pass the --debug flag to view the state of your component instance in case the deployment failed for any reason.

```bash
serverless info
```

### 4. Remove

If you wanna tear down your entire infrastructure that was created during deployment, 
just run `serverless remove` and serverless will remove all the data it needs from the built-in state storage system to delete only the relevant cloud resources that it created.

```bash
serverless remove
```

### TODOs
1. Better Error Management.
2. Store and consume messages through Dynamo DB.