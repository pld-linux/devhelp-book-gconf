Summary:	DevHelp book: gconf
Summary(pl):	Ksi±¿ka do DevHelpa o gconfie
Name:		devhelp-book-gconf
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/gconf.tar.gz
# Source0-md5:	3df7a075494c01520fb282b25683c2a1
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about gconf.

%description -l pl
Ksi±¿ka do DevHelpa o gconfie.

%prep
%setup -q -c -n gconf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/gconf,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/gconf.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/gconf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
