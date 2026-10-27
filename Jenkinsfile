
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/sakshishirke412/mlops-iris-demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Retrain Model') {
            steps {
                sh './venv/bin/python retrain.py'
            }
        }

        stage('Deploy Model') {
            steps {
                sh '''
                    mkdir -p /var/lib/jenkins/app
                    cp iris_model.pkl /var/lib/jenkins/app/iris_model.pkl
                    ls -lh /var/lib/jenkins/app/iris_model.pkl
                '''
            }
        }
    }
}
