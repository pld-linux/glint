Summary:	Graphical front-end for RPM
Summary(pl):	Graficzna nak³adka na RPM
Name:		glint
Version:	2.6.1
Release:	1
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Icon:		rpm.gif
Source:		%{name}-%{version}.tar.gz
Source1:	%{name}.wmconfig
Patch:		%{name}-make.patch
Requires:	python >= 1.4, pythonlib >= 1.12, zlib
BuildRoot:	/tmp/%{name}-%{version}

%description
Glint is a graphical interface to the RPM package management tool. It allows
you to browse packages installed on your system, verify and query those 
package. It allows allows you to update packages with new versions and
install
new packages.

%description -l pl
Glint jest graficznym interfejsem dla RPM. Pozwala na przegl±danie
pakietów zainstalowanych w systemie, ich weryfikowanie i odpytywanie. Daje
tak¿e mo¿liwo¶æ uaktualniania pakietów i instalowania nowych.

%prep
%setup -q
%patch -p1

%build
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/glint

strip $RPM_BUILD_ROOT/usr/lib/python1.5/lib-dynload/*

gzip -9nf $RPM_BUILD_ROOT/usr/man/man8/glint.8

%files
%defattr(644, root, root, 755)

%doc COPYING
%config(missingok) /etc/X11/wmconfig/glint

%attr(755, root, root) /usr/bin/glint
/usr/lib/rhs/glint
/usr/lib/rhs/control-panel/*
%attr(755, root, root) /usr/lib/python1.5/lib-dynload/*
%attr(644, root, man)  /usr/man/man8/*

%changelog
* Sun Jan 24 1999 Micha³ Kuratczyk <kurkens@polbox.com>
- built for PLD
