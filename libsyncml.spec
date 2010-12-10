%define libmajor 0
%define libname %mklibname syncml %libmajor
%define develname %mklibname syncml -d

Name:		libsyncml
Version:	0.4.6
Release:	%mkrel 7
Summary:	C library implementation of the SyncML protocol
License:	LGPLv2+
Group:		System/Libraries
URL:		http://libsyncml.opensync.org/
Source:		http://libsyncml.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
Patch0:		libsyncml-0.4.6-gobject.patch
BuildRequires:	wbxml-devel
BuildRequires:	openobex-devel
# Specifically needs 2.2 not 2.4 - AdamW 2008/08
BuildRequires:	libsoup-2.2-devel
BuildRequires:	bluez-devel
BuildRequires:	cmake
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
C library implementation of the SyncML protocol

%package -n %{libname}
License:	LGPLv2+
Group:		System/Libraries
Summary:	C library implementation of the SyncML protocol

%description -n %{libname}
C library implementation of the SyncML protocol.

This package is required by applications using the Syncml library
implementation of SyncML.

%package -n %{develname}
License:	LGPLv2+
Group:		System/Libraries
Summary:	Development package for C library implementation of the SyncML protocol
Requires:	%libname = %version-%release
Obsoletes:	%{mklibname syncml 0}-devel
Provides:	%name-devel = %version-%release
Provides:	syncml-devel = %version-%release

%description -n %{develname}
C library implementation of the SyncML protocol

This package is required to compile applications that use the Syncml
library implementation of SyncML

%prep
%setup -q
%patch0 -p1 -b .gobject

%build
%cmake
%make

%install
rm -Rf %{buildroot}
cd build
%makeinstall_std
cd -

%clean
rm -Rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%{_bindir}/syncml-http-server
%{_bindir}/syncml-http-client
%{_bindir}/syncml-obex-client
#%{_mandir}/man1/syncml-http-server.1*
#%{_mandir}/man1/syncml-obex-client.1*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.%{libmajor}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/%{name}-1.0
%{_libdir}/*.so
#%{_libdir}/*.la
%{_libdir}/pkgconfig/libsyncml*.pc
