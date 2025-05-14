pipeline {
    agent any
    stages {
        stage('Check for Git Changes') {
            steps {
                script {
                    def changes = sh(script: 'git diff --name-only HEAD~1 HEAD', returnStdout: true).trim()
                    if (changes) {
                        echo "Changes detected:\n${changes}"
                        sh 'python 2_a_star_graph.py'
                    } else {
                        echo 'No changes detected. Skipping 2_a_star_graph.py execution.'
                    }
                }
            }
        }
    }
}