#
%define		_module_name	slideshow

Summary:	Enlightenment DR17 module: %{_module_name}
Summary(pl.UTF-8):	Moduł Enlightenmenta DR17: slideshow
Name:		enlightenment-module-%{_module_name}
Version:	0.0.7
Release:	1
License:	BSD-like
Group:		X11/Window Managers/Tools
Source0:	http://www.get-e.org/Resources/Modules/_files/%{_module_name}-%{version}.tar.gz
# Source0-md5:	e20b828f71d0df75b67f63a2d9be63c8
URL:		http://www.get-e.org/Resources/Modules/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje
BuildRequires:	enlightenment-devel
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
Requires:	enlightenment
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Very simple Enlightenment DR17 module used to change desktop
backgrounds.

%description -l pl.UTF-8
Bardzo prosty moduł Enlightenmenta DR17 służący do zmiany tła pulpitu.

%prep
%setup -q -n %{_module_name}
sed -e 's|datadir=.*|datadir="`enlightenment-config --module-dir`/${PACKAGE}"|' \
    -e '/PACKAGE_DATA_DIR/s|"[^"]*"|"`enlightenment-config --module-dir`/${PACKAGE}"|' \
    -e '/PACKAGE_LIB_DIR/s|"[^"]*"|"`enlightenment-config --module-dir`"|' \
    -i configure.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING INSTALL README TODO
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name}
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name}/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules_extra/%{_module_name}/linux-gnu-*/module.so
# violates FHS
%{_libdir}/enlightenment/modules_extra/%{_module_name}/*.edj
%{_libdir}/enlightenment/modules_extra/%{_module_name}/module_icon.png
