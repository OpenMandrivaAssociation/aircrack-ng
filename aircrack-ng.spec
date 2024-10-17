Name:		aircrack-ng
Version:	1.7
Release:	1
Summary:	Reliable 802.11 (wireless) sniffer and WEP key cracker
License:	GPLv2+
Group:		Networking/Other
URL:		https://www.aircrack-ng.org/doku.php
Source0:	http://download.aircrack-ng.org/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:  ethtool
BuildRequires:	pkgconfig(libnl-3.0)

%description
aircrack-ng is a set of tools for auditing wireless networks. It's an 
enhanced/reborn version of aircrack. It consists of airodump (an 802.11 
packet capture program), aireplay (an 802.11 packet injection program), 
aircrack (static WEP and WPA-PSK cracking), airdecap (decrypts WEP/WPA 
capture files), and some tools to handle capture files (merge, convert, 
etc.).

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -O3"
export LDFLAGS="%{ldflags}"
sh autogen.sh
%configure
%make_build datadir=%{_datadir} unstable=true sqlite=true

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/%{name}

# At this time, there don't seem to be any projects
# trying to use aircrack-ng's headers. Not much of
# a point in shipping headers for internal libraries.
rm -rf %{buildroot}%{_includedir}

%files
%doc ChangeLog README AUTHORS
%{_libdir}/libaircrack*.so
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_mandir}/man8/*.8*
%dir %{_datadir}/aircrack-ng
