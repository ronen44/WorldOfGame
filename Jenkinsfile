pipeline {
    agent any

    stages {
        stage('ChcekOut') {
            steps {
               git url: 'https://github.com/ronen44/WorldOfGame.git' , branch: 'master'
            }
        }
        stage('Build') {
            steps {
               sh 'docker build -t ronen44/maingame:0.1 .'
            }
        }
        stage('run') {
            steps {
               sh 'docker run -d --name game -p 5000:5000 ronen44/maingame:0.1 '
            }
        }
        stage('test') {
            steps {
               sh 'docker exec -d game python e2e.py '
            }
        }
    }
}
