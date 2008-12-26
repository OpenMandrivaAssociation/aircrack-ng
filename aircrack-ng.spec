%define name    aircrack-ng	
%define version 1.0
%define release %mkrel 0.rc1.1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Reliable 802.11 (wireless) sniffer and WEP key cracker
License:	GPL
Group:		Networking/Other
URL:		http://www.aircrack-ng.org/doku.php
Source:		http://download.aircrack-ng.org/%{name}-%{version}-rc1.tar.gz
Patch0:		1085.patch
Patch1:		1177.patch
Patch2:		1222.patch
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
aircrack-ng is a set of tools for auditing wireless networks. It's an 
enhanced/reborn version of aircrack. It consists of airodump (an 802.11 
packet capture program), aireplay (an 802.11 packet injection program), 
aircrack (static WEP and WPA-PSK cracking), airdecap (decrypts WEP/WPA 
capture files), and some tools to handle capture files (merge, convert, 
etc.).

%prep
%setup -q -n %{name}-%{version}-rc1
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
export CFLAGS="%optflags"
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall

mkdir %{buildroot}%_mandir/man1
mv %{buildroot}%_mandir/*.1 %{buildroot}%_mandir/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README AUTHORS INSTALLING LICENSE VERSION 
%_bindir/*
%_sbindir/*
%_mandir/man1/*


