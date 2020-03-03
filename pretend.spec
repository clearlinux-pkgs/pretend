#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD1B3ADC0E0238CA6 (alex.gaynor@gmail.com)
#
Name     : pretend
Version  : 1.0.9
Release  : 41
URL      : http://pypi.debian.net/pretend/pretend-1.0.9.tar.gz
Source0  : http://pypi.debian.net/pretend/pretend-1.0.9.tar.gz
Source1  : http://pypi.debian.net/pretend/pretend-1.0.9.tar.gz.asc
Summary  : A library for stubbing in Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pretend-license = %{version}-%{release}
Requires: pretend-python = %{version}-%{release}
Requires: pretend-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
pretend
=======

.. image:: https://secure.travis-ci.org/alex/pretend.png
    :target: https://travis-ci.org/alex/pretend

Pretend is a library to make stubbing with Python easier.

What is stubbing?
-----------------

Stubbing is a technique for writing tests. You may hear the term mixed up with
mocks, fakes, or doubles. Basically a stub is an object that returns pre-canned
responses, rather than doing any computation.

Martin Fowler does a good job explaining the terms in his `Mocks Aren't Stubs`_
article.

.. _`Mocks Aren't Stubs`: http://martinfowler.com/articles/mocksArentStubs.html

How do I install ``pretend``?
-----------------------------

It's easy with ``pip``!

.. code:: bash

    $ pip install pretend

How do I use ``pretend``?
-------------------------

It's easy, the ``stub`` function makes it easy to create a stub:

.. code:: pycon

    >>> from pretend import stub
    >>> x = stub(country_code="US")
    >>> some_function(x)

Here ``x`` will be an object with a single attribute ``country_code`` which has
the value ``"US"``. Unlike mocks, ``x`` will not respond to any other attribute
or methods, nor does it have any methods for making assertions about what you
accessed.

If you want to add a method to the stub, simply provide a function to it:

.. code:: pycon

    >>> from pretend import stub
    >>> x = stub(country_code=lambda: "US")
    >>> x.country_code()
    'US'

It's important to note that functions on stubs *do not* take a ``self``
argument, this is because stubs should be returning pre-canned values, not
doing computations.

Exceptions with ``pretend``
---------------------------

Sometimes a method you want to stub doesn't return a value, but instead raises
an exception. To make this easy, ``pretend`` provides a helper function,
``raiser``, it can be used like so:

.. code:: pycon

    >>> from pretend import stub, raiser
    >>> x = stub(func=raiser(ValueError))
    >>> x.func()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "pretend.py", line 74, in inner
        raise exc
    ValueError

Why is stubbing better?
-----------------------

Ideally stubbing tests how your system responds to a particular input, rather
than which API is used. Stubbing still requires you to write tests that check
the results of a computation, rather than looking for side effects. This
doesn't always work though, so you do sometimes still need mocking (e.g.
sometimes you really want to check for a side effect.)

How do I get my stub into place?
--------------------------------

If you come from other mocking libraries you're probably used to a ``patch``
method to put a mock in place. ``pretend`` doesn't include anything like this,
a) we believe it's better, where possible, to pass stubs as arguments rather
than monkey patch them into place, b) we believe that when you do need to
monkey patch something into place you should use something provided by your
testing tool. ``py.test`` includes `such a tool`_.

.. _`such a tool`: http://pytest.org/latest/monkeypatch.html

What if I really need to record the calls?
------------------------------------------

If you really really need to, ``pretend`` includes a ``call_recorder`` utility:

.. code:: pycon

    >>> from pretend import call_recorder, call
    >>> f = call_recorder(lambda a: a + 2)
    >>> f(3)
    5
    >>> assert f.calls == [call(3)]

Who wrote this?
---------------

``pretend`` is by Alex Gaynor, who was just tired of not having a good stubbing
tool for Python. The name is from Idan Gazit.

%package license
Summary: license components for the pretend package.
Group: Default

%description license
license components for the pretend package.


%package python
Summary: python components for the pretend package.
Group: Default
Requires: pretend-python3 = %{version}-%{release}

%description python
python components for the pretend package.


%package python3
Summary: python3 components for the pretend package.
Group: Default
Requires: python3-core
Provides: pypi(pretend)

%description python3
python3 components for the pretend package.


%prep
%setup -q -n pretend-1.0.9
cd %{_builddir}/pretend-1.0.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583203073
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pretend
cp %{_builddir}/pretend-1.0.9/LICENSE.rst %{buildroot}/usr/share/package-licenses/pretend/b8244d638801c0e229ef021afd04594e09f113f3
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pretend/b8244d638801c0e229ef021afd04594e09f113f3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
