#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pretend
Version  : 1.0.8
Release  : 10
URL      : https://pypi.python.org/packages/source/p/pretend/pretend-1.0.8.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pretend/pretend-1.0.8.tar.gz
Summary  : A library for stubbing in Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pretend-python
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
pretend
=======
.. image:: https://secure.travis-ci.org/alex/pretend.png
:target: https://travis-ci.org/alex/pretend

%package python
Summary: python components for the pretend package.
Group: Default

%description python
python components for the pretend package.


%prep
%setup -q -n pretend-1.0.8

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
