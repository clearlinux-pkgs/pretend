#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x125F5C67DFE94084 (alex.gaynor@gmail.com)
#
Name     : pretend
Version  : 1.0.8
Release  : 17
URL      : http://pypi.debian.net/pretend/pretend-1.0.8.tar.gz
Source0  : http://pypi.debian.net/pretend/pretend-1.0.8.tar.gz
Source99 : http://pypi.debian.net/pretend/pretend-1.0.8.tar.gz.asc
Summary  : A library for stubbing in Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pretend-legacypython
Requires: pretend-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=======

%package legacypython
Summary: legacypython components for the pretend package.
Group: Default

%description legacypython
legacypython components for the pretend package.


%package python
Summary: python components for the pretend package.
Group: Default
Requires: pretend-legacypython

%description python
python components for the pretend package.


%prep
%setup -q -n pretend-1.0.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505055960
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1505055960
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
