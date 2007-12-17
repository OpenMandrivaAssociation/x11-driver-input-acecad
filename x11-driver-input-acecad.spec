Name: x11-driver-input-acecad
Version: 1.2.1
Release: %mkrel 2
Summary: X.org input driver for Acecad Flair devices
Group: Development/X11

########################################################################
# git clone git//git.mandriva.com/people/pcpa/xorg/drivers/xf86-input-acecad  xorg/drivers/xf86-input-acecad
# cd xorg/drivers/xf86-input-acecad
# git-archive --format=tar --prefix=xf86-input-acecad-1.2.1/ master | bzip2 -9 > xf86-input-acecad-1.2.1.tar.bz2
########################################################################
Source0: xf86-input-acecad-%{version}.tar.bz2
License: GPLv2+ and MIT

########################################################################
# git-format-patch master..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: libsysfs-devel

Conflicts: xorg-x11-server < 7.0

%description
Acecad is an Xorg input driver for Acecad Flair devices.
THIS DRIVER IS CONSIDERED BROKEN AND SHOULD BE FIXED
SOON, AS IT USES dlopen and dclose TO ACCESS LINUX
SPECIFIC LIBRARIES, IN THIS CASE libsysfs.so.

%prep
%setup -q -n xf86-input-acecad-%{version}

%patch1 -p1

%build
autoreconf -ifs
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


