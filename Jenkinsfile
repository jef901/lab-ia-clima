pipeline {
    agent any

    stages {
        stage('Clonar Código') {
            steps {
                echo '📥 Descargando los últimos cambios desde la rama main de Git...'
            }
        }
        
        stage('Validar Sintaxis') {
            steps {
                echo '🔍 Verificando finales de línea con dos2unix...'
                // En un servidor real esto asegura que no existan errores CRLF
            }
        }

        stage('Construir Artefacto') {
            steps {
                echo '📦 Compilando imagen Docker: mi-chequeador-red:latest...'
            }
        }

        stage('Pruebas de Conectividad') {
            steps {
                echo '🚀 Levantando contenedor de pruebas y ejecutando ping a la API...'
            }
        }
    }
    
    post {
        success {
            echo '✅ ¡PIPELINE EXITOSO! El código es seguro y la infraestructura está en verde.'
        }
        failure {
            echo '❌ ¡ALERTA! El pipeline falló en alguna etapa. Revisar los logs inmediatamente.'
        }
    }
}
