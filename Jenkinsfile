pipeline {
    agent any

    stages {
        stage('📥 Clonar Código') {
            steps {
                echo 'Descargando la última versión del repositorio...'
                checkout scm
            }
        }
        
        stage('🧪 Pruebas en Contenedor') {
            steps {
                echo 'Levantando contenedor dinámico de Python para correr Pytest...'
                sh '''
                docker run --rm -v $(pwd):/app -w /app python:3.12-slim sh -c "
                pip install --no-cache-dir pytest &&
                pytest test_app.py
                "
                '''
            }
        }
        
        stage('📦 Empaquetar Artefacto') {
            steps {
                echo 'Empaquetando la aplicación para producción...'
                sh 'tar -czvf app_produccion.tar.gz app.py'
            }
        }
    }
    
    post {
        success {
            echo '💾 Guardando el Artefacto en el servidor de Jenkins...'
            archiveArtifacts artifacts: 'app_produccion.tar.gz', followSymlinks: false
            echo '✅ ¡PIPELINE EXITOSO!'
        }
        failure {
            echo '❌ ¡PIPELINE FALLIDO! Las pruebas no pasaron.'
        }
    }
}
