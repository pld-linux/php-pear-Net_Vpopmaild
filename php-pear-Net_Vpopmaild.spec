%define		_class		Net
%define		_subclass	Vpopmaild
%define		_status		beta
%define		_pearname	Net_Vpopmaild
Summary:	%{_pearname} - Class for accessing Vpopmail's vpopmaild daemon
Summary(pl.UTF-8):	%{_pearname} - klasa dostępu do demona vpopmaild
Name:		php-pear-%{_pearname}
Version:	0.3.2
Release:	3
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d8ea0aa72062af4e52af9629d47e039f
URL:		http://pear.php.net/package/Net_Vpopmaild/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Log
Requires:	php-pear-Net_Socket
Requires:	php-pear-PEAR-core >= 1:1.4.0
Obsoletes:	php-pear-Net_Vpopmaild-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Supports all vpopmaild commands, such as adding/removing domains,
users, robots (autoresponders), and ezmlm lists (todo), as well as
modifying domain limits, IP maps, etc

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten obsługuje wszystkie polecenia vpopmaild, takie jak
dodawanie i usuwanie domen, użytkowników, robotów (autoresponderów),
czy list ezmlm, jak również modyfikowanie limitów, mapowań adresów IP
itd.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Net_Vpopmaild/{docs,examples}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/Vpopmaild
%{php_pear_dir}/Net/Vpopmaild.php
