pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/daniaalkhmous99/Final-Project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t final-project .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f final-container || true'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 --name final-container final-project'
            }
        }
    }
}