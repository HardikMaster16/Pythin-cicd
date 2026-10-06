pipeline {
  agent any
 
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
 
    stage('Install') {
      steps {
        sh '''
          python3 -m venv .venv
          . .venv/bin/activate
          pip install -r requirements.txt
        '''
      }
    }
 
    stage('Test') {
      steps { sh '. .venv/bin/activate && python -m pytest --junitxml=report.xml' }
      post { always { junit 'report.xml' } }
    }
 
    stage('Docker Build') {
      steps { sh 'docker build -t demo-app:${BUILD_NUMBER} -t demo-app:latest .' }
    }
 
    stage('Deploy') {
      steps {
        sh '''
          docker rm -f demo-app || true
          docker run -d --name demo-app --restart unless-stopped -p 8000:8000 demo-app:latest
        '''
      }
    }
 
    stage('Health Check') {
      steps {
        sh '''
          sleep 5
          docker exec demo-app python -c "import urllib.request; print(urllib.request.urlopen('http://localhost:8000/health').read())"
        '''
      }
    }
  }
 
  post {
    success { echo 'Deployed! Open http://<server-ip>:8000' }
    failure { echo 'Pipeline failed - check the red stage' }
  }
}
