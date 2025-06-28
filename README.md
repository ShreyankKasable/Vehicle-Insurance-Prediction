# 🚗 MLOps Project - Vehicle Insurance Prediction Pipeline

Welcome to the **Vehicle Insurance MLOps Project** — a comprehensive end-to-end machine learning pipeline designed to automate, scale, and deploy predictive models for vehicle insurance classification. This project showcases practical implementation of **MLOps** principles including modular coding, cloud integration, CI/CD automation, and API deployment.

---

## 📁 Project Setup and Structure

### ✅ Step 1: Generate Template

* Run `template.py` to scaffold the project structure with necessary folders and files.

### ✅ Step 2: Package Management

* Define local package structure using `setup.py` and `pyproject.toml`.
* 📄 See `crashcourse.txt` to understand these files.

### ✅ Step 3: Create and Activate Virtual Environment

```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
```

* Verify packages with:

```bash
pip list
```

---

## 📊 MongoDB Setup and Data Management

### 🔧 Step 4: Setup MongoDB Atlas

1. Create a MongoDB Atlas account and M0 cluster.
2. Set up a DB user and whitelist IP as `0.0.0.0/0`.
3. Get the connection string for Python driver and update the password.

### 📄 Step 5: Push Dataset to MongoDB

* Create `notebook/mongoDB_demo.ipynb`, add your dataset and write code to upload it.
* Verify your uploaded data in Atlas > Browse Collections.

---

## 📝 Logging, Exception Handling, and EDA

### 📌 Step 6: Setup Logging and Exception Handling

* Create reusable logging and exception utilities.
* Test them in `demo.py`.

### 📈 Step 7: Perform EDA and Feature Engineering

* Analyze patterns and prepare features in your `EDA` notebook under `notebook/`.

---

## 📥 Data Ingestion

### 🔄 Step 8: Create Data Ingestion Pipeline

* Define:

  * MongoDB logic in `configuration.mongo_db_connections.py`
  * Raw data logic in `data_access/proj1_data.py`
  * Ingestion logic in `components.data_ingestion.py`
* Define config and artifact classes:

  * `entity/config_entity.py`
  * `entity/artifact_entity.py`

### 🌐 Step 9: Set MongoDB URL

```bash
# For Bash
export MONGODB_URL="mongodb+srv://<username>:<password>...."

# For PowerShell
$env:MONGODB_URL = "mongodb+srv://<username>:<password>...."
```

---

## 🔍 Data Validation, Transformation & Model Training

### ✅ Step 10: Data Validation

* Add schema in `config/schema.yaml`
* Add validation logic in `utils/main_utils.py`

### ✅ Step 11: Data Transformation

* Build transformation code in `components/data_transformation.py`
* Add estimator logic in `entity/estimator.py`

### ✅ Step 12: Model Training

* Use transformed data to train models in `components/model_trainer.py`

---

## ☁️ AWS Setup for Model Evaluation & Deployment

### 🔐 Step 13: Configure AWS

1. Create IAM user with `AdministratorAccess`
2. Export AWS keys as environment variables:

```bash
export AWS_ACCESS_KEY_ID="your_key"
export AWS_SECRET_ACCESS_KEY="your_secret"
```

### 🩢 Step 14: Model Registry using S3

* Create S3 bucket: `my-model-mlopsproj`
* Use:

  * `cloud_storage/aws_storage.py`
  * `entity/s3_estimator.py`
  * `constants/__init__.py` for bucket info

---

## 🚀 Model Evaluation, Pushing, and Prediction

### ✅ Step 15: Evaluate & Push Best Model

* Use `components/model_evaluation.py` and `model_pusher.py`

### 🌐 Step 16: Create FastAPI Prediction App

* Setup `app.py` with routes:

  * `/training`: Train pipeline
  * `/predict`: Make predictions

### 🧱 Step 17: Add Static Files

* Create `static/` and `template/` directories for frontend if needed

---

## 🔄 CI/CD Automation with GitHub Actions, Docker, EC2

### 🐳 Step 18: Dockerize

* Create:

  * `Dockerfile`
  * `.dockerignore`

### 🧷 Step 19: GitHub Actions

* Setup `.github/workflows/aws.yaml`
* Add GitHub Secrets:

  * `AWS_ACCESS_KEY_ID`
  * `AWS_SECRET_ACCESS_KEY`
  * `ECR_REPO`
  * `AWS_DEFAULT_REGION`

### 🗂️ Step 20: EC2 & Self-Hosted Runner

1. Launch EC2 (Ubuntu 24.04, T2 Medium)
2. Install Docker:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

3. Register EC2 as GitHub Runner

### 🌐 Step 21: Open EC2 Port

* Go to EC2 > Security > Edit Inbound Rules

  * Add: Custom TCP | Port 5080 | Source: 0.0.0.0/0

### ✅ Step 22: Access Application

* Visit: `http://<your-ec2-public-ip>:5080`

---

## 🧱 Folder Structure

```bash
.
├── app.py
├── demo.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── setup.py
├── pyproject.toml
├── notebook/
│   └── mongoDB_demo.ipynb
├── config/
│   ├── schema.yaml
│   └── model.yaml
└── src/
    ├── components/
    ├── configuration/
    ├── cloud_storage/
    ├── data_access/
    ├── constants/
    ├── entity/
    ├── exception/
    ├── logger/
    ├── pipeline/
    └── utils/
```

---

## 🛠️ Tech Stack

* **Python 3.10**
* **MongoDB Atlas**
* **FastAPI**
* **Scikit-learn**, **Pandas**, **NumPy**
* **Docker**, **GitHub Actions**, **EC2**, **S3**, **ECR**

---

## 🎯 End-to-End Workflow

```text
Data Ingestion ➞ Data Validation ➞ Data Transformation ➞ Model Training ➞
Model Evaluation ➞ Model Registry (S3) ➞ Deployment (EC2 + FastAPI + Docker) ➞ CI/CD Pipeline
```

---

## 💬 Author

**Shreyank Kasable**

🌐 \[https://github.com/ShreyankKasable]

If you found this project helpful, don’t forget to ⭐ the repo!
