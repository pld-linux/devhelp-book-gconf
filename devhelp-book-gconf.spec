Summary:	DevHelp book: gconf
Summary(pl):	Ksi±¿ka do DevHelp'a o gconf
Name:		devhelp-book-gconf
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/gconf.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about gconf

%description -l pl
Ksi±¿ka do DevHelp o gconf

%prep
%setup -q -c gconf -n gconf

%build
mv -f book gconf
mv -f book.devhelp gconf.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/gconf
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install gconf.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install gconf/* $RPM_BUILD_ROOT%{_prefix}/books/gconf

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
