Name: x11-driver-input-acecad
Version: 1.2.1
Release: %mkrel 4
Summary: X.org input driver for Acecad Flair devices
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-acecad-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: libsysfs-devel

Conflicts: xorg-x11-server < 7.0

Patch1: 0001-acecad-don-t-crash-when-xf86IsCorePointer-is-not-de.patch
Patch2: 0002-acecad-do-our-own-scaling-with-USB-device-since-it.patch
Patch3: 0003-acecad-set-type_name-to-XI_TABLET.patch
Patch4: 0004-acecad-fake-device-limits-screen-limits-in-xserv.patch

%description
Acecad is an Xorg input driver for Acecad Flair devices.

%prep
%setup -q -n xf86-input-acecad-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%configure2_5x

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/acecad_drv.la
%{_libdir}/xorg/modules/input/acecad_drv.so
%{_mandir}/man4/acecad.*
