Name: x11-driver-input-acecad
Version: 1.5.0
Release: 6
Summary: X.org input driver for Acecad Flair devices
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-acecad-%{version}.tar.bz2
License: MIT

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: libsysfs-devel

Requires: x11-server-common %(xserver-sdk-abi-requires xinput)

Conflicts: xorg-x11-server < 7.0

%description
Acecad is an Xorg input driver for Acecad Flair devices.

%prep
%setup -qn xf86-input-acecad-%{version}

%build
%configure2_5x

%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/input/acecad_drv.so
%{_mandir}/man4/acecad.*
