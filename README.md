SuperKart Churn Prediction & Deployment Platform

An end-to-end, production-grade MLOps pipeline demonstrating model optimization and full-stack operationalization via containerized environments.

Business Problem & Objective
* The Problem: 
SuperKart is facing increased market competition resulting in an upward trend in customer churn. Manually identifying defection patterns within large transactional datasets is inefficient, directly impacting revenue predictability and long-term customer lifetime value (LTV).

* The Objective:
To build and deploy an end-to-end predictive analytics pipeline that handles comprehensive data preprocessing, feature engineering, and outlier treatment. The final productionized model isolates high-risk churn profiles, enabling corporate stakeholders to deploy targeted retention campaigns.

Architecture & Operational Infrastructure
The application features a fully decoupled system design built for high availability and structural separation of concerns:
* Backend Inference Engine:
Powered by a customized **Flask API** that handles real-time route requests, model weight storage, and **batch inference capabilities**.
**Frontend Client:** An interactive interface built natively with **Streamlit** that routes processing inputs to the backend API and presents clean, forward-facing insights.
**Containerization & Environment Execution:** Fully packaged using a production-ready **Dockerfile** for the backend to isolate systems dependencies and streamline cloud orchestration.


Data flow:
┌────────────────────────┐    Flask API Request    ┌────────────────────────┐
│  Frontend (Streamlit)  │ ──────────────────────> │  Backend Engine (Flask)│
│ User Input & Analytics │ <────────────────────── │ Model Weights & Docker │
└────────────────────────┘    Batch Inference      └────────────────────────┘


Technical Stack
** Languages & Core Architecture:
Python, Flask API, Streamlit
**Data Engineering Workflow:
Feature Engineering, Outlier Treatment, Custom Preprocessing Pipelines
**DevOps & Containerization:
Docker (Backend Containerization), GitHub Sandbox Environments
**Machine Learning Engine:
Two distinct, optimized ML models subjected to Hyperparameter Tuning and serialization.


Setup & Local Execution
1. Clone this repository to your local environment.
2. Build and launch the containerized backend layer:
   ```bash
   docker build -t superkart-backend ./backend


Run the Streamlit presentation interface from the root directory:
bash
streamlit run frontend/app.py


