%define	svnrev	r1926

Name:		aircrack-ng
Version:	1.1
Release:	4.%{svnrev}.1
Summary:	Reliable 802.11 (wireless) sniffer and WEP key cracker
License:	GPLv2+
Group:		Networking/Other
URL:		http://www.aircrack-ng.org/doku.php
Source0:	http://download.aircrack-ng.org/%{name}-%{version}.%{svnrev}.tar.xz
Patch0:		aircrack-ng-1.1.r1926-makefile-fixes.patch
Patch1:		aircrack-ng-1.1.r1926-airodump-oui-destdir.patch
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	sqlite3-devel

%description
aircrack-ng is a set of tools for auditing wireless networks. It's an 
enhanced/reborn version of aircrack. It consists of airodump (an 802.11 
packet capture program), aireplay (an 802.11 packet injection program), 
aircrack (static WEP and WPA-PSK cracking), airdecap (decrypts WEP/WPA 
capture files), and some tools to handle capture files (merge, convert, 
etc.).

%prep
%setup -q
%patch0 -p1 -b .make_makeup~
%patch1 -p1 -b .oui_destdir~

%build
export CFLAGS="%{optflags} -O3"
export LDFLAGS="%{ldflags}"
%make datadir=%{_datadir} unstable=true sqlite=true

%install
%{__rm} -rf %{buildroot}
%makeinstall unstable=true sqlite=true

mkdir -p %{buildroot}%{_datadir}/%{name}
touch %{buildroot}%{_datadir}/%{name}/airodump-ng-oui.txt

%clean
%{__rm} -rf %{buildroot}

%post 
%{_sbindir}/airodump-ng-oui-update

%files
%defattr(-,root,root)
%doc ChangeLog README AUTHORS VERSION 
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man1/*.1*
%dir %{_datadir}/aircrack-ng
%ghost %{_datadir}/aircrack-ng/airodump-ng-oui.txt


%changelog
* Fri Jul 08 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1-4.r1926.1
+ Revision: 689296
- update to latest code from svn to get --ignore-negative-one workaround, which
  tends to be required to make aircrack work with ~most drivers

* Thu Jun 16 2011 Jani Välimaa <wally@mandriva.org> 1.1-3
+ Revision: 685691
- run airodump-ng-oui-update in %%post (redo P1)
- install wesside-ng and some other unstable utils (mdv#61298)
- properly use LDFLAGS (redo P0)
- drop buildroot definition

* Thu Aug 05 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1-2mdv2011.0
+ Revision: 566451
- work around kinda broken parallell build
- really fix path to oui data file
  * build unstable utils as well
- fix path of oui data, and download it during %%install
-DHAVE_REGEXP has to be passed to preprocessor to have any effect, not linker...
- ditch redundant docs..
- fix mandir and make use of pkg-config etc. in makefiles (P0)
- build with sqlite support
- cosmetics
  * don't lower upstream -O3 optimizations

* Sun Apr 25 2010 Funda Wang <fwang@mandriva.org> 1.1-1mdv2010.1
+ Revision: 538569
- New version 1.1

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 1.0-2mdv2010.1
+ Revision: 537607
- rebuild

* Wed Sep 09 2009 Pascal Terjan <pterjan@mandriva.org> 1.0-1mdv2010.0
+ Revision: 434936
- Update to 1.0 final

* Mon Aug 03 2009 Frederik Himpe <fhimpe@mandriva.org> 1.0-0.rc.4.2mdv2010.0
+ Revision: 408569
- Disable parallel make to fix build
- Update to new version 1.0-rc4
- Remove patch integrated upstream

* Thu Mar 12 2009 Emmanuel Andry <eandry@mandriva.org> 1.0-0.rc2.1mdv2009.1
+ Revision: 354287
- fix 64 bits build with gentoo patch
- New version 1.0 rc2
- drop patches (merged upstream)
- fix license

* Fri Dec 26 2008 Pascal Terjan <pterjan@mandriva.org> 1.0-0.rc1.1mdv2009.1
+ Revision: 319499
- BuildRequires zlib-devel
- BuildRequires openssl-devel
- Update to 1.0-rc1

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.9.3-3mdv2009.0
+ Revision: 243049
- rebuild
- rebuild

* Sat Mar 01 2008 Michael Scherer <misc@mandriva.org> 0.9.3-1mdv2008.1
+ Revision: 177233
- update to new version 0.9.3

* Wed Feb 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.2-1mdv2008.1
+ Revision: 162976
- update to new version 0.9.2

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jul 27 2007 Pascal Terjan <pterjan@mandriva.org> 0.9.1-1mdv2008.0
+ Revision: 56245
- update to new version 0.9.1

* Wed May 23 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.9-1mdv2008.0
+ Revision: 30215
- update to 0.9

* Fri Apr 27 2007 Lenny Cartier <lenny@mandriva.org> 0.8-1mdv2008.0
+ Revision: 18543
- Update to 0.8


* Sun Jan 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.7-1mdv2007.0
+ Revision: 111232
- new version

* Wed Nov 15 2006 Lenny Cartier <lenny@mandriva.com> 0.6.2-1mdv2007.1
+ Revision: 84554
- Update to 0.6.2
- Import aircrack-ng

* Tue Aug 29 2006 Lenny Cartier <lenny@mandriva.com> 0.6.1-1mdv2007.0
- 0.6.1

* Tue Jun 27 2006 Austin Acton <austin@mandriva.org> 0.6-1mdk
- New release 0.6
- build opts

* Wed May 10 2006 Lenny Cartier <lenny@mandriva.com> 0.5-1mdk
- new

