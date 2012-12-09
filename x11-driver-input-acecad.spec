Name: x11-driver-input-acecad
Version: 1.5.0
Release: 5
Summary: X.org input driver for Acecad Flair devices
Group: System/X11
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-acecad-%{version}.tar.bz2
License: MIT

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: sysfsutils-devel

Requires: x11-server-common %(xserver-sdk-abi-requires xinput)

Conflicts: xorg-x11-server < 7.0

%description
Acecad is an Xorg input driver for Acecad Flair devices.

%prep
%setup -q -n xf86-input-acecad-%{version}

%build
%configure2_5x

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%{_libdir}/xorg/modules/input/acecad_drv.so
%{_mandir}/man4/acecad.*


%changelog
* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.5.0-1mdv2011.0
+ Revision: 683595
- New version 1.5.0.
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-4
+ Revision: 671119
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.4.0-3mdv2011.0
+ Revision: 595754
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.4.0-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Tue Nov 10 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.4.0-1mdv2010.1
+ Revision: 464243
- New version: 1.4.0

* Thu Feb 26 2009 Thierry Vignaud <tv@mandriva.org> 1.3.0-1mdv2009.1
+ Revision: 345053
- new release
- fix group

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.2.2-2mdv2009.0
+ Revision: 225943
- rebuild

* Thu Feb 14 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2.2-1mdv2008.1
+ Revision: 168618
- Update to latest upstream release 1.2.2.
  RPM patches removed as they are already applied in latest version.

* Wed Jan 30 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2.1-4mdv2008.1
+ Revision: 160472
- Revert to use only upstream tarballs and only mandatory patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.2.1-3mdv2008.1
+ Revision: 156566
- re-enable rpm debug packages support

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Dont dlopen libsysfs.so, just link with it and call functions as appropriate.
      Add patch to mandriva+custom branch.
    - Remove -devel package as it isn't really required as it provides only 2 files
      that aren't even header files; still don't install the .la files.
      All dependency files should be stored in the x11-util-modular package as they
      are only required for the "modular" build.
    - Move .la files to new -devel package, and also add .deps files to -devel package.
    - URL was removed in a previous commit.
    - Update package to use specific tag xf86-input-acecad-1.2.1
      Unfortunately, this is one of the few modules that have a version tag.
      The new patches are the new diff and considered correct patches. Actually,
      if these patches are not applied, this module will have unresolved symbols,
      and incompatible with xserver 1.4.
    - Fix comment documentation, an ending / required for git-archive --prefix
      argument, otherwise it will not create the named directory, but instead
      append file names to the prefix.
    - Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 11 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.2.1-1mdv2008.1
+ Revision: 97056
- new upstream version: 1.2.1
- minor spec cleanup

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages

* Mon Apr 30 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.2.0-3mdv2008.0
+ Revision: 19568
- Add build-requirement for libsysfs2
  This new driver version includes support for device 'semi-hotplugging'
  via /sysfs. See the driver announcement for details on how to enable it:
  http://lists.freedesktop.org/archives/xorg-announce/2007-April/000301.html

* Mon Apr 30 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.2.0-1mdv2008.0
+ Revision: 19464
- Updated to 1.2.0.

* Thu Apr 26 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.1-1mdv2008.0
+ Revision: 18425
- new upstream version: 1.1.1


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-30 16:03:02 (31708)
- fill in summary & descriptions for all input drivers

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 19:59:30 (31594)
- Updated drivers for X11R7.1

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

