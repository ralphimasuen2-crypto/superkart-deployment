Project Overview

An end-to-end machine learning deployment project demonstrating the integration of predictive modeling, a Flask REST API, a Streamlit user interface, and Docker-based backend containerization.

The application predicts product sales using a trained machine learning pipeline and supports both individual and batch predictions.

Business Problem & Objective

Businesses need reliable sales predictions to support inventory planning, product allocation, and operational decision-making.

Objective: Develop and deploy a predictive analytics application that processes product and store information and generates sales predictions through an accessible user interface.

Solution Architecture

The application separates the frontend interface from the backend inference service.

* Machine Learning Pipeline: Uses a serialized model pipeline to generate predictions from input features.
* Backend Inference Engine: A Flask API loads the trained model and handles prediction requests.
* Frontend Application: Streamlit provides interactive inputs, CSV uploads, and prediction-result displays.
* Containerization: Docker packages the backend and its dependencies for a reproducible execution environment.

Data Flow

User Input / CSV Upload
          |
          v
   Streamlit Frontend
          |
          v
     Flask REST API
          |
          v
 Preprocessing & Model Inference
          |
          v
     Prediction Results
          |
          v
  Results Displayed in Streamlit

Key Features

* Individual product-sales prediction.
* Batch inference using uploaded CSV files.
* Flask REST API integration.
* Serialized machine learning pipeline using Joblib.
* Interactive Streamlit interface.
* Docker-based backend containerization.
* Version-controlled source code and project documentation.

API Endpoints

Method	Endpoint	Purpose
GET	/	Returns a welcome message
POST	/v1/predict	Generates an individual prediction
POST	/v1/predictbatch	Generates predictions for an uploaded CSV file

The batch endpoint expects the uploaded file under the form field name file.

Technology Stack

Category	Technologies
Programming language	Python
Data processing	Pandas, NumPy
Machine learning	Scikit-learn, XGBoost
Backend	Flask, Gunicorn
Frontend	Streamlit
Model serialization	Joblib
Containerization	Docker
Version control and development	GitHub, GitHub Codespaces

Repository Structure

superkart-deployment/
├── backend/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── superkart_model.joblib
├── frontend/
│   ├── app.py
│   └── requirements.txt
└── README.md

Setup and Execution

Prerequisites

* Python
* Git
* Docker

1. Clone the Repository

git clone https://github.com/ralphimasuen2-crypto/superkart-deployment.git
cd superkart-deployment

2. Build the Backend Docker Image

From the repository root:

docker build -t superkart-backend ./backend

3. Run the Backend Container

docker run -d --name superkart-backend -p 7860:7860 superkart-backend

The backend listens on port 7860 and uses Gunicorn to serve the Flask application.

4. Configure Frontend Connectivity

The Streamlit application currently uses the backend URL:

BACKEND_URL = "http://backend:7860"

This hostname must resolve from the frontend environment. For local execution, configure the frontend to use a reachable backend address, such as http://localhost:7860, when appropriate. For containerized execution, ensure the frontend and backend share a network on which the backend service name resolves.

5. Run the Streamlit Frontend

From the repository root, install the frontend dependencies specified in frontend/requirements.txt, then run:

streamlit run frontend/app.py

Open the local URL displayed by Streamlit in your browser.

Note: The commands document the intended execution workflow. A fresh-environment setup should be tested before treating these instructions as independently verified.

Learning Outcomes & Technical Contributions

This project demonstrates practical application of:

* Data preparation and preprocessing.
* Feature engineering and outlier treatment.
* Machine learning model development and evaluation.
* Model serialization and inference.
* REST API development.
* Frontend and backend integration.
* Individual and batch prediction workflows.
* Docker-based backend packaging.
* GitHub-based source control and technical documentation.

Business Value

The application demonstrates how machine learning can be integrated into a usable software application to support sales forecasting and data-driven operational decisions.

Actual business impact depends on model performance, data quality, and validation in the intended operating environment.

Project Status

The repository contains the backend inference application, Streamlit frontend, serialized model, dependency files, Docker configuration, and project documentation.

The project demonstrates the workflow from model development to application-level inference and deployment.

Author

Raphael Imasuen

AI/ML | Predictive Analytics | Python | Machine Learning Deployment

GitHub: ralphimasuen2-crypto
