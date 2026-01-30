pipeline {
    agent any 

    parameters {
        string(name: 'MEM_THRESHOLD', defaultValue: '4000', description: 'Threshold in MB to fail build')
    }

    stages {
        stage('Setup Environment') {
            steps {
                // Install psutil if not present
                sh 'pip install --user psutil'
            }
        }

        stage('Monitor Memory') {
            steps {
                script {
                    // Run the script and capture output
                    sh "python3 memory_check.py"
                }
            }
        }
    }

    post {
        failure {
            echo "Build failed because a process is consuming too much memory."
            // You could add Slack/Email notifications here
        }
    }
}