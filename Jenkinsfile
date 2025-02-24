pipeline {
    agent any

    environment {
        REGISTRY = "image-registry.openshift-image-registry.svc:5000"
        PROJECT = "aedingbo-dev"
        IMAGE_NAME = "order-api"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/aedingbo/order-api.git'
            }
        }

        stage('Build and Test') {
            agent {
                kubernetes {
                    yaml """
                    apiVersion: v1
                    kind: Pod
                    metadata:
                      labels:
                        build: maven
                    spec:
                      containers:
                      - name: maven
                        image: maven:3.8.5-openjdk-11
                        command: ["sleep"]
                        args: ["infinity"]
                    """
                }
            }
            steps {
                container('maven') {
                    sh 'mvn clean package'
                }
            }
        }

        stage('Build Image') {
            steps {
                sh """
                oc start-build ${IMAGE_NAME} --from-dir=. --follow
                """
            }
        }

        stage('Deploy to OpenShift') {
            steps {
                sh """
                oc rollout latest dc/${IMAGE_NAME}
                """
            }
        }
    }
}