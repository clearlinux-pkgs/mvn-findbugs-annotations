PKG_NAME := mvn-findbugs-annotations
URL = https://github.com/stephenc/findbugs-annotations/archive/findbugs-annotations-1.3.9-1.tar.gz
ARCHIVES = https://repo1.maven.org/maven2/com/github/stephenc/findbugs/findbugs-annotations/1.3.9-1/findbugs-annotations-1.3.9-1.jar : https://repo1.maven.org/maven2/com/github/stephenc/findbugs/findbugs-annotations/1.3.9-1/findbugs-annotations-1.3.9-1.pom : https://repo1.maven.org/maven2/com/google/code/findbugs/annotations/2.0.3/annotations-2.0.3.jar : https://repo1.maven.org/maven2/com/google/code/findbugs/annotations/2.0.3/annotations-2.0.3.pom : 

include ../common/Makefile.common
