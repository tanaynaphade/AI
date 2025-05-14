pipeline {
    agent any
    stages {
        stage('Run 2_a_star_graph.py on Git Changes') {
            steps {
                echo "Changes detected in the Git repository."
                sh 'python3 2_a_star_graph.py'
            }
        }
    }
}