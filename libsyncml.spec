%define libmajor 0
%define libname %mklibname syncml %libmajor

Name:		libsyncml
Version:	0.4.4
Release:	%mkrel 1
Summary:	C library implementation of the SyncML protocol
License:	LGPL
Group:		System/Libraries
URL:		http://libsyncml.opensync.org/
Source:		svn://svn.opensync.org/libsyncml/trunk/%{name}-%{version}.tar.bz2
Patch:      %{name}-0.4.4-cflags.patch
BuildRequires:	wbxml2-devel
BuildRequires:	openobex-devel
BuildRequires:	libsoup-devel > 2.2.7-1mdk
BuildRequires:	bluez-devel
Requires:	%libname = %version
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
C library implementation of the SyncML protocol

%package -n %libname
License:	LGPL
Group:		System/Libraries
Summary:	C library implementation of the SyncML protocol

%description -n %libname
C library implementation of the SyncML protocol.

This package is required by applications using the Syncml library
implementation of SyncML.

%package -n %{libname}-devel
License:	LGPL
Group:		System/Libraries
Summary:	Development package for C library implementation of the SyncML protocol
Requires:	%libname = %version-%release
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
C library implementation of the SyncML protocol

This package is required to compile applications that use the Syncml
library implementation of SyncML

%prep
%setup -q
%patch -p 1

%build
autoreconf
%configure2_5x
%make

%install
rm -Rf %{buildroot}
%makeinstall_std

%clean
rm -Rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/syncml-http-server
%{_bindir}/syncml-http-client
%{_bindir}/syncml-obex-client
%{_mandir}/man1/syncml-http-server.1*
%{_mandir}/man1/syncml-obex-client.1*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/%{name}-1.0
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/libsyncml*.pc
