%include	/usr/lib/rpm/macros.php
%define		_class		MDB2
%define		_subclass	Driver_oci8
%define		_status		stable
%define		_pearname	MDB2_Driver_oci8

Summary:	%{_pearname} - oci8 MDB2 driver
Summary(pl.UTF-8):   %{_pearname} - sterownik oci8 dla MDB2
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b6ad76f73672bf7ccf44b9ea05eac941
URL:		http://pear.php.net/package/MDB2_Driver_oci8/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(oci8)
Requires:	php-common >= 3:4.3.0
Requires:	php-pear
Requires:	php-pear-MDB2 >= 2.0.0-0.beta6
Requires:	php-pear-PEAR-core >= 1:1.0b1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Oracle OCI8 MDB2 driver.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Sterownik Oracle OCI8 dla MDB2.

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
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/MDB2/Driver/Datatype/oci8.php
%{php_pear_dir}/MDB2/Driver/Function/oci8.php
%{php_pear_dir}/MDB2/Driver/Manager/oci8.php
%{php_pear_dir}/MDB2/Driver/Native/oci8.php
%{php_pear_dir}/MDB2/Driver/Reverse/oci8.php
%{php_pear_dir}/MDB2/Driver/oci8.php
