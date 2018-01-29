#!groovy

pipeline {
   agent { label 'android-builder' }

   parameters {
      string(name: 'ghprbActualCommit', defaultValue: 'master', description: 'When starting build give the sha1 parameter commit id you want to build or refname (eg: origin/pr/9/head).')
   }

   environment {
      TEST_RESULT_LOCATION    = "**/*-nosetests.xml"
      MOBILE_APP_VERSION      = "${BUILD_NUMBER}"
      PYTHONPATH              ="${WORKSPACE}:${PYTHONPATH}"
      JAVA_HOME               ="/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.151-1.b12.amzn2.x86_64"
      ANDROID_HOME            = "/var/lib/android"
      GRADLE_HOME             ="/opt/gradle/gradle-4.5"
      PATH                    ="$PATH:${GRADLE_HOME}/bin:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin"
   }

   stages {

      stage('Unit Test') { // for display purposes
         steps {

            // Checkout code
            checkout([
               $class: 'GitSCM', 
               userRemoteConfigs: [[
                     url: 'https://github.com/WolkOps/MobileApp_Demo.git', 
                     name: 'origin',
                     refspec: '+refs/heads/master:refs/remotes/origin/master'
               ]],
               branches: [[name: "${params.ghprbActualCommit}"]],
               extensions: [
                  [$class: 'WipeWorkspace'] // wipe workspace before clone
               ]
             ])

            sh '''
            #!/bin/bash
            set -e

            # Build android app
            npm install
            ionic cordova build android --prod --release -- -- --minSdkVersion=21

            # Show the apk
            ls -ltrha ${WORKSPACE}/platforms/android/app/build/outputs/apk/release/app-release-unsigned.apk

            # zip -r test_bundle.zip tests/ wheelhouse/ requirements.txt

            '''
         }         
      }
   }

   post{
      always {
         // Print that pipeline is finished
         echo 'Pipeline done, recording results and cleaning up environment...'

      }
   }
}