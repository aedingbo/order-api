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

        stage('Build and Package') {
            steps {
                sh 'echo "Skipping Maven build, no pom.xml required"'
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
                 #!/bin/bash
        oc rollout restart deployment/${IMAGE_NAME}
                """
            }
        }
    }
}
