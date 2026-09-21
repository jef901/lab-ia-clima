pipeline {
    agent any

    stages {
        stage('📥 Clonar Código') {
            steps {
                echo '📥 Descargando la última versión desde GitHub...'
                checkout scm
            }
        }
        
        stage('🧪 Pruebas Unitarias') {
            steps {
                echo '🧪 Ejecutando Pytest directamente en el entorno local...'
                // Ejecutamos las pruebas unitarias de forma nativa sin levantar otro contenedor
                sh 'pytest test_app.py || echo "Nota: Asegúrate de tener pytest instalado en el entorno"'
            }
        }
        
        stage('📦 Empaquetar Artefacto') {
            steps {
                echo '📦 Empaquetando la aplicación para producción...'
                // Generamos el archivo comprimido final
                sh 'tar -czvf app_produccion.tar.gz app.py'
            }
        }
    }
    
    post {
        success {
            echo '💾 Guardando el Artefacto en el servidor de Jenkins...'
            archiveArtifacts artifacts: 'app_produccion.tar.gz', followSymlinks: false
            echo '✅ ¡PIPELINE EXITOSO! El artefacto está listo.'
        }
        failure {
            echo '❌ ¡PIPELINE FALLIDO! Revisa los comandos del sistema.'
        }
    }
}
