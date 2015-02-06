Name:		x11-driver-input-acecad
Version:	1.5.0
Release:	16
Summary:	X.org input driver for Acecad Flair devices
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-acecad-%{version}.tar.bz2

BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-server-devel >= 1.12
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	sysfsutils-devel
Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)

%description
Acecad is an Xorg input driver for Acecad Flair devices.

%prep
%setup -qn xf86-input-acecad-%{version}
autoreconf -fiv

%build
%configure2_5x

%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/input/acecad_drv.so
%{_mandir}/man4/acecad.*

