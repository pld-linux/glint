Summary:	Graphical front-end for RPM
Summary(pl):	Graficzna nak³adka na RPM
Name:		glint
Version:	2.6.1
Release:	3
License:	GPL
Group:		Applications/System
Icon:		rpm.gif
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	0e50b38644f9082a7bac55da4274f0aa
Source1:	%{name}.wmconfig
Patch0:		%{name}-make.patch
BuildRequires:	python-devel
BuildRequires:	rpm-devel
Requires:	python >= 1.4, pythonlib >= 1.12, zlib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glint is a graphical interface to the RPM package management tool. It
allows you to browse packages installed on your system, verify and
query those package. It allows allows you to update packages with new
versions and install new packages.

%description -l pl
Glint jest graficznym interfejsem dla RPM. Pozwala na przegl±danie
pakietów zainstalowanych w systemie, ich weryfikowanie i odpytywanie.
Daje tak¿e mo¿liwo¶æ uaktualniania pakietów i instalowania nowych.

%prep
%setup -q
%patch -p1

%build
%{__make} CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/glint

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(missingok) %{_sysconfdir}/X11/wmconfig/glint

%attr(755,root,root) %{_bindir}/glint
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/*
%{_libdir}/rhs/glint
%{_libdir}/rhs/control-panel/*
%{_mandir}/man8/*
