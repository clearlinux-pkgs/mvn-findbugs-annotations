#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-findbugs-annotations
Version  : 1.3.9.1
Release  : 5
URL      : https://github.com/stephenc/findbugs-annotations/archive/findbugs-annotations-1.3.9-1.tar.gz
Source0  : https://github.com/stephenc/findbugs-annotations/archive/findbugs-annotations-1.3.9-1.tar.gz
Source1  : https://repo1.maven.org/maven2/com/github/stephenc/findbugs/findbugs-annotations/1.3.9-1/findbugs-annotations-1.3.9-1.jar
Source2  : https://repo1.maven.org/maven2/com/github/stephenc/findbugs/findbugs-annotations/1.3.9-1/findbugs-annotations-1.3.9-1.pom
Source3  : https://repo1.maven.org/maven2/com/google/code/findbugs/annotations/2.0.1/annotations-2.0.1.jar
Source4  : https://repo1.maven.org/maven2/com/google/code/findbugs/annotations/2.0.1/annotations-2.0.1.pom
Source5  : https://repo1.maven.org/maven2/com/google/code/findbugs/annotations/2.0.3/annotations-2.0.3.jar
Source6  : https://repo1.maven.org/maven2/com/google/code/findbugs/annotations/2.0.3/annotations-2.0.3.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-findbugs-annotations-data = %{version}-%{release}

%description
Introduction
------------
This is a cleanroom implementation of the Findbugs Annotations.

%package data
Summary: data components for the mvn-findbugs-annotations package.
Group: Data

%description data
data components for the mvn-findbugs-annotations package.


%prep
%setup -q -n findbugs-annotations-findbugs-annotations-1.3.9-1

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/stephenc/findbugs/findbugs-annotations/1.3.9-1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/github/stephenc/findbugs/findbugs-annotations/1.3.9-1/findbugs-annotations-1.3.9-1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/stephenc/findbugs/findbugs-annotations/1.3.9-1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/github/stephenc/findbugs/findbugs-annotations/1.3.9-1/findbugs-annotations-1.3.9-1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/code/findbugs/annotations/2.0.1
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/google/code/findbugs/annotations/2.0.1/annotations-2.0.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/code/findbugs/annotations/2.0.1
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/google/code/findbugs/annotations/2.0.1/annotations-2.0.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/code/findbugs/annotations/2.0.3
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/com/google/code/findbugs/annotations/2.0.3/annotations-2.0.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/code/findbugs/annotations/2.0.3
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/com/google/code/findbugs/annotations/2.0.3/annotations-2.0.3.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/github/stephenc/findbugs/findbugs-annotations/1.3.9-1/findbugs-annotations-1.3.9-1.jar
/usr/share/java/.m2/repository/com/github/stephenc/findbugs/findbugs-annotations/1.3.9-1/findbugs-annotations-1.3.9-1.pom
/usr/share/java/.m2/repository/com/google/code/findbugs/annotations/2.0.1/annotations-2.0.1.jar
/usr/share/java/.m2/repository/com/google/code/findbugs/annotations/2.0.1/annotations-2.0.1.pom
/usr/share/java/.m2/repository/com/google/code/findbugs/annotations/2.0.3/annotations-2.0.3.jar
/usr/share/java/.m2/repository/com/google/code/findbugs/annotations/2.0.3/annotations-2.0.3.pom
