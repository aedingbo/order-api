# Order API - CI/CD with Jenkins & OpenShift

## Overview

This project implements a CI/CD pipeline using Jenkins and OpenShift to automate the deployment of a Python-based Order API. The pipeline performs the following steps:

- Code Checkout from GitHub
- Building and Packaging (No `pom.xml` required)
- Building a Docker Image and pushing it to OpenShift
- Deploying the application to OpenShift

---

## Technology Stack

### CI/CD and Deployment
- Jenkins (Pipeline Automation)
- OpenShift (Containerized Deployment)
- GitHub (Source Code Management)
- Docker (Containerization)
- PowerShell & OpenShift CLI (oc) – Managing OpenShift resources
  
### Application Stack
- Python 3.9
- Flask (Lightweight API framework)

---

## Project Hierarchy
order-api/ 
│── .venv/ # Virtual Environment (ignored in Git) 
│── app.py # Main API script 
│── Dockerfile # Instructions for building the container 
│── Jenkinsfile # CI/CD pipeline configuration for Jenkins 
│── jenkins-template.yaml # OpenShift Jenkins template 
│── README.md # Project Documentation (this file)
