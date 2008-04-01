%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Vpopmaild
%define		_status		alpha
%define		_pearname	Net_Vpopmaild
Summary:	%{_pearname} - Class for accessing Vpopmail's vpopmaild daemon
Summary(pl.UTF-8):	%{_pearname} - klasa dostępu do demona vpopmaild
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	2
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	17d677de1edfa04c4b57b10b30672d04
URL:		http://pear.php.net/package/Net_Vpopmaild/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Log
Requires:	php-pear-Net_Socket
Requires:	php-pear-PEAR >= 1.4.0b1
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

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

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

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Net_Vpopmaild
