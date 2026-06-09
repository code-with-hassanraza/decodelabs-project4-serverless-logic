# ⚡ Project 4 — The Serverless Logic
### DecodeLabs Cloud Computing Internship | Batch 2026

![AWS](https://img.shields.io/badge/AWS-Lambda-orange?logo=amazon-aws)
![Python](https://img.shields.io/badge/Python-3.14-green?logo=python)
![Serverless](https://img.shields.io/badge/Serverless-FaaS-blueviolet)
![CloudWatch](https://img.shields.io/badge/CloudWatch-Logs-blue?logo=amazon-aws)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📋 Scenario
A company wants to build a simple Cost Calculator API. Running a traditional
server 24/7 just for this small calculation is wastefully expensive. The mission:
deploy code without managing any infrastructure — a solution that only runs when
triggered and costs exactly $0 when idle.

---

## 🎯 Mission Accomplished
- ✅ Deployed a serverless Cost Calculator API on AWS Lambda
- ✅ Wrote Python 3.14 function accepting a JSON payload with two numbers
- ✅ Function calculates the sum and returns a clean JSON response
- ✅ Attached IAM Execution Role (Principle of Least Privilege)
- ✅ Ran 3 test events — all passed with correct results
- ✅ Verified millisecond billing in Amazon CloudWatch logs

---

## 🏗️ Architecture

```
     JSON Payload Trigger
     {"num1": 15, "num2": 25}
            │
            ▼
┌───────────────────────────────┐
│         AWS Lambda            │
│   cost-calculator-decodelabs  │
│                               │
│   Runtime: Python 3.14        │
│   Architecture: ARM64         │
│   Memory: 128 MB              │
│   Timeout: 3 sec              │
│                               │
│   def lambda_handler():       │
│       num1 + num2 = total     │
│       return {"Sum": total}   │
└───────────┬───────────────────┘
            │
            ▼
     JSON Response
     {"statusCode": 200, "Sum": 40}
            │
            ▼
   Amazon CloudWatch Logs
   (Permanent execution record)
```

**Model:** FaaS (Function as a Service) | Pay-per-execution | Zero idle cost

---

## 📁 Repository Structure

```
decodelabs-project4-serverless-logic/
├── README.md
├── lambda/
│   └── lambda_function.py
├── tests/
│   ├── test-event-1.json
│   ├── test-event-2.json
│   └── test-event-3.json
└── screenshots/
    ├── 01-lambda-function-created.png
    ├── 02-code-deployed.png
    ├── 03-test1-result-sum40.png
    ├── 04-test2-result-sum300.png
    ├── 05-test3-result-sum10.png
    └── 06-cloudwatch-logs.png
```

---

## 🐍 Lambda Function Code

```python
import json

def lambda_handler(event, context):

    # Extract the two numbers from the incoming JSON payload
    num1 = event.get('num1', 0)
    num2 = event.get('num2', 0)

    # Calculate the sum
    total = num1 + num2

    # Return a clean JSON response
    return {
        'statusCode': 200,
        'Sum': total,
        'message': f'Cost Calculator: {num1} + {num2} = {total}'
    }
```

---

## 🧪 Test Events & Results

| Test Event | JSON Input | Expected Sum | Actual Sum | Billed Duration | Status |
|---|---|---|---|---|---|
| TestSum1 | `{"num1": 15, "num2": 25}` | 40 | **40** | 8 ms | ✅ Passed |
| TestSum2 | `{"num1": 100, "num2": 200}` | 300 | **300** | 10 ms | ✅ Passed |
| TestSum3 | `{"num1": 7, "num2": 3}` | 10 | **10** | 13 ms | ✅ Passed |

---

## ⚙️ Lambda Configuration

| Setting | Value |
|---|---|
| Function Name | cost-calculator-decodelabs |
| Runtime | Python 3.14 |
| Architecture | ARM64 (Graviton2) |
| Memory | 128 MB |
| Max Billed Duration | 13 ms |
| Idle Cost | $0.00 |
| Region | us-east-1 |
| IAM Role | AWSLambdaBasicExecutionRole |

---

## 💰 Cost Comparison

| Model | Billing | Idle Cost | Best For |
|---|---|---|---|
| EC2 (t3.micro) | Per hour (~$0.0116/hr) | Yes — pays 24/7 | Always-on workloads |
| AWS Lambda | Per millisecond | **Zero** | Event-driven tasks |

> **This function's 3 test runs cost a fraction of a cent combined.**

---

## 📊 CloudWatch Log Output (Sample)

```
START RequestId: 027d65e7-191e-4925-acd1-385fad290584 Version: $LATEST
END   RequestId: 027d65e7-191e-4925-acd1-385fad290584
REPORT RequestId: 027d65e7-...  Duration: 7.09 ms  Billed Duration: 8 ms
Memory Size: 128 MB  Max Memory Used: 40 MB
```

---

## 📸 Screenshots
> See the `/screenshots` folder for step-by-step visual proof of the entire setup.

---

## 🛠️ Technologies Used
- **AWS Lambda** — Serverless compute platform
- **Python 3.14** — Function runtime
- **IAM Execution Role** — Least-privilege permissions
- **Amazon CloudWatch** — Execution logging and monitoring
- **AWS Console Test Events** — Mock API invocation

---

## 👤 Author
**Muhammad Hassan Raza**
Cloud Computing Intern @ DecodeLabs | Batch 2026
