pipeline {
    agent any

    stage('📥 Clonar Código') {
    steps {
        echo '📥 Verificación Exitosa: ¡Este es el Pipeline Real de Septiembre de 2026! 🚀'
        checkout scm
    }
}
        
        stage('🧪 Pruebas en Contenedor') {
            steps {
                echo 'Levantando contenedor dinámico de Python para correr Pytest...'
                // Ejecutamos pytest dentro de un contenedor aislado con la app y el test actuales
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
                // Comprimimos nuestra app en un archivo ejecutable zip
                sh 'tar -czvf app_produccion.tar.gz app.py'
            }
        }
    }
    
    post {
        success {
            echo '💾 Guardando el Artefacto en el servidor de Jenkins...'
            // Jenkins almacena de forma permanente el archivo comprimido final
            archiveArtifacts artifacts: 'app_produccion.tar.gz', followSymlinks: false
            echo '✅ ¡PIPELINE EXITOSO!'
        }
        failure {
            echo '❌ ¡PIPELINE FALLIDO! Las pruebas no pasaron.'
        }
    }
}

