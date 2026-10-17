
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/yeldss2164/taipakov-yeldos-devops.git'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m compileall -q app'
                sh 'echo "Build completed successfully"'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -s tests -p "test_*.py"'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t taipakov-yeldos-devops .'
            }
        }

        stage('Docker Run') {
            steps {
                sh 'docker rm -f taipakov-yeldos-ci || true'
                sh 'docker run -d --name taipakov-yeldos-ci taipakov-yeldos-devops'
                sh 'sleep 3'
                sh 'docker logs taipakov-yeldos-ci'
                sh 'docker logs taipakov-yeldos-ci | grep -q "Application is running successfully!"'
            }
        }
    }
}
