%define debug_package	%{nil}

Name: x11-driver-input-acecad
Version: 1.2.1
Release: %mkrel 2
Summary: X.org input driver for Acecad Flair devices
Group: Development/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-input-acecad  xorg/drivers/xf86-input-acecad
# cd xorg/drivers/xf86-input-acecad
# git-archive --format=tar --prefix=xf86-input-acecad-1.2.1/ xf86-input-acecad-1.2.1 | bzip2 -9 > xf86-input-acecad-1.2.1.tar.bz2
########################################################################
Source0: xf86-input-acecad-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-input-acecad-1.2.1..origin/mandriva+gpl
Patch1: 0001-acecad-don-t-crash-when-xf86IsCorePointer-is-not-de.patch
Patch2: 0002-acecad-do-our-own-scaling-with-USB-device-since-it.patch
Patch3: 0003-acecad-set-type_name-to-XI_TABLET.patch
Patch4: 0004-acecad-fake-device-limits-screen-limits-in-xserv.patch
Patch5: 0005-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-util-macros		>= 1.1.5-4mdk
#BuildRequires: gcc			>= 4.2.2
#BuildRequires: glibc-devel		>= 2.7.1
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: libsysfs-devel
#>= 2.1.0
BuildRequires: x11-server-devel		>= 1.4
Conflicts: xorg-x11-server < 7.0

%description
Acecad is an Xorg input driver for Acecad Flair devices.

%prep
%setup -q -n xf86-input-acecad-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/input/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/acecad_drv.so
%{_mandir}/man4/acecad.*
