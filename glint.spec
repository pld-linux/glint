Summary:	Graphical front-end for RPM
Summary(pl):	Graficzna nak�adka na RPM
Name:		glint
Version:	2.6.1
Release:	2d
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Icon:		rpm.gif
Source:		%{name}-%{version}.tar.gz
Source1:	glint.wmconfig
Patch:		glint-make.patch
Requires:	python >= 1.4, pythonlib >= 1.12, zlib
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Glint is a graphical interface to the RPM package management tool. It allows
you to browse packages installed on your system, verify and query those 
package. It allows allows you to update packages with new versions and
install new packages.

%description -l pl
Glint jest graficznym interfejsem dla RPM. Pozwala na przegl�danie
pakiet�w zainstalowanych w systemie, ich weryfikowanie i odpytywanie. Daje
tak�e mo�liwo�� uaktualniania pakiet�w i instalowania nowych.

%prep
%setup -q
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s \
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/glint

strip $RPM_BUILD_ROOT/usr/lib/python1.5/lib-dynload/*

gzip -9nf $RPM_BUILD_ROOT/usr/man/man8/*

%files
%defattr(644,root,root,755)
%config(missingok) /etc/X11/wmconfig/glint

%attr(755,root, root) /usr/bin/glint

/usr/lib/rhs/glint
/usr/lib/rhs/control-panel/*

%attr(755,root,root) /usr/lib/python1.5/lib-dynload/*
%attr(644,root, man) /usr/man/man8/*

%changelog
* Tue Feb  9 1999 Micha� Kuratczyk <kurkens@polbox.com>
  [2.6-2d]
- added using $RPM_OPT_FLAGS and LDFLAGS=-s
- sloted BuildRoot into PLD standard

* Mon Jan 25 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.6.1-1d]
- added "rm -rf $RPM_BUILD_ROOT" on top %install.
- other cosmetic changes.

* Sun Jan 24 1999 Micha� Kuratczyk <kurkens@polbox.com>
- built for PLD
