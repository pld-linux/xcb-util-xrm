Summary:	XCB util-xrm module
Name:		xcb-util-xrm
Version:	1.2
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/Airblader/xcb-util-xrm/releases/download/v%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	242dfd4af757fc5ca0e952a714b9606a
URL:		https://github.com/Airblader/xcb-util-xrm
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxcb-devel >= 1.4
BuildRequires:	pkgconfig
BuildRequires:	xcb-proto >= 1.6
BuildRequires:	xcb-util-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros >= 1.16
Requires:	libxcb >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

XCB util-xrm module provides the following library:
- xrm: utility functions for the X resource manager

%package devel
Summary:	Header files for XCB util-xrm library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxcb-devel >= 1.4

%description devel
Header files for XCB util-xrm library.

%package static
Summary:	Static XCB util-xrm library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XCB util-xrm library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libxcb-xrm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-xrm.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb-xrm.so
%{_libdir}/libxcb-xrm.la
%{_includedir}/xcb/xcb_xrm.h
%{_pkgconfigdir}/xcb-xrm.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxcb-xrm.a
