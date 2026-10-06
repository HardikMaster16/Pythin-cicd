pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                bat '''
                    py -m venv .venv
                    .venv\\Scripts\\python.exe -m pip install --upgrade pip
                    .venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                    .venv\\Scripts\\python.exe -m pytest --junitxml=report.xml
                '''
            }
            post {
                always {
                    junit 'report.xml'
                }
            }
        }

        stage('Docker Build') {
            steps {
                bat '''
                    docker build -t demo-app:%BUILD_NUMBER% -t demo-app:latest .
                '''
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                    docker rm -f demo-app 2>NUL
                    docker run -d --name demo-app --restart unless-stopped -p 8000:8000 demo-app:latest
                '''
            }
        }

        stage('Health Check') {
            steps {
                bat '''
                    timeout /t 5 /nobreak >NUL
                    docker exec demo-app python -c "import urllib.request; print(urllib.request.urlopen('http://localhost:8000/health').read())"
                '''
            }
        }
    }

    post {
        success {
            echo 'Deployed! Open http://localhost:8000'
        }
        failure {
            echo 'Pipeline failed - check the red stage'
        }
    }
}