Summary:	Graphical front-end for RPM
Summary(pl):	Graficzna nak³adka na RPM
Name:		glint
Version:	2.6.1
Release:	3
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Icon:		rpm.gif
Source:		%{name}-%{version}.tar.gz
Source1:	glint.wmconfig
Patch:		glint-make.patch
BuildRequires:	rpm-devel
BuildRequires:	python-devel
Requires:	python >= 1.4, pythonlib >= 1.12, zlib
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Glint is a graphical interface to the RPM package management tool. It allows
you to browse packages installed on your system, verify and query those 
package. It allows allows you to update packages with new versions and
install new packages.

%description -l pl
Glint jest graficznym interfejsem dla RPM. Pozwala na przegl±danie
pakietów zainstalowanych w systemie, ich weryfikowanie i odpytywanie. Daje
tak¿e mo¿liwo¶æ uaktualniania pakietów i instalowania nowych.

%prep
%setup -q
%patch -p1

%build
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/glint

strip $RPM_BUILD_ROOT%{_libdir}/python1.5/lib-dynload/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/*

%files
%defattr(644,root,root,755)
%config(missingok) /etc/X11/wmconfig/glint

%attr(755,root,root) %{_bindir}/glint
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/*
%{_libdir}/rhs/glint
%{_libdir}/rhs/control-panel/*
%{_mandir}/man8/*
