Summary:	XCB util-xrm module
Summary(pl.UTF-8):	Moduł XCB util-xrm
Name:		xcb-util-xrm
Version:	1.3
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/Airblader/xcb-util-xrm/releases/download/v%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	6b5249f1e4e4e1c5e367d894d27dd0c0
URL:		https://github.com/Airblader/xcb-util-xrm
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake
BuildRequires:	libtool
# xcb xcb-aux
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

%description -l pl.UTF-8
xcb-util udostępnia wiele bibliotek opartych powyżej libxcb (głównej
biblioteki protokołu X) oraz trochę bibliotek rozszerzeń. Te
eksperymentalne biblioteki udostępniają wygodne funkcje i interfejsy
czyniące surowy protokół X bardziej używalnym. Niektóre biblioteki
udostępniają także kod kliencki nie będący ściśle częścią protokołu X,
ale tradycyjnie dostarczany przez Xlib.

Moduł XCB util-xrm dostarcza bibliotekę:
- xrm: funkcje narzędziowe dla zarządcy zasobów X

%package devel
Summary:	Header files for XCB util-xrm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki XCB util-xrm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxcb-devel >= 1.4

%description devel
Header files for XCB util-xrm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki XCB util-xrm.

%package static
Summary:	Static XCB util-xrm library
Summary(pl.UTF-8):	Biblioteka statyczna XCB util-xrm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XCB util-xrm library.

%description static -l pl.UTF-8
Biblioteka statyczna XCB util-xrm.

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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libxcb-xrm.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libxcb-xrm.so.*.*.*
%ghost %{_libdir}/libxcb-xrm.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libxcb-xrm.so
%{_includedir}/xcb/xcb_xrm.h
%{_pkgconfigdir}/xcb-xrm.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxcb-xrm.a
