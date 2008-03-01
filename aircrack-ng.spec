%define name    aircrack-ng	
%define version 0.9.3
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Reliable 802.11 (wireless) sniffer and WEP key cracker
License:    GPL
Group:      Networking/Other
URL:        http://www.aircrack-ng.org/doku.php
Source:     http://download.aircrack-ng.org/%{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
aircrack-ng is a set of tools for auditing wireless networks. It's an 
enhanced/reborn version of aircrack. It consists of airodump (an 802.11 
packet capture program), aireplay (an 802.11 packet injection program), 
aircrack (static WEP and WPA-PSK cracking), airdecap (decrypts WEP/WPA 
capture files), and some tools to handle capture files (merge, convert, 
etc.).

%prep
%setup -q

%build
%make "CFLAGS=%optflags"

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


