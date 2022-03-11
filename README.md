## Introduction

This project deploys a telegram bot applications to AWS' serverless infrastructure - Lambda, using the Serverless Framework Component.
The application will never charge for idle time, and require little-to-zero administration.

## Quick Start

### 1. Install

```bash
# Install Serverless Framework
npm install -g serverless
```

### 2. Deploy

You can use following command to deploy the APP.

```bash
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

### Setting up credentials (Optional)

```bash
# Add your Tencent credentials here
touch .env
```

```
# .env file
TELEGRAM_TOKEN=123
AWS_ACCESS_KEY_ID=123
AWS_SECRET_ACCESS_KEY=123
```
