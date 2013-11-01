#
%define		_state		stable
%define		orgname		printer-applet
%define		qtver		4.8.0

Summary:	K Desktop Environment - printer applet
Name:		kde4-printer-applet
Version:	4.11.3
Release:	1
License:	GPL
Group:		X11/Applications
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
Source0:	http://ixion.pld-linux.org/~arekm/kde/%{orgname}-%{version}.tar.xz
# Source0-md5:	8acbc3ac369d29dd8f4511c4bffd638b
URL:		http://www.kde.org/
BuildRequires:	automoc4
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	python-pycups
BuildRequires:	qt4-build
BuildRequires:	system-config-printer
Requires:	kde4-kdebase-workspace >= %{version}
Requires:	python-PyKDE4
Requires:	python-pycups
Requires:	system-config-printer
Obsoletes:	kde4-kdeutils-printer-applet
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Printer Applet is a system tray utility that shows current print jobs,
shows printer warnings and errors.

%description -l pl.UTF-8
Printer Applet to narzedzie zasobnika systemowego, ktore pokazuje
aktualne zadania drukarki, ostrzezenia i bledy.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DINSTALL_PRINTER_APPLET=TRUE \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%{_bindir}/printer-applet
%dir %{_datadir}/apps/printer-applet
%{_datadir}/apps/printer-applet/authconn.py
%{_datadir}/apps/printer-applet/debug.py
%{_datadir}/apps/printer-applet/monitor.py
%{_datadir}/apps/printer-applet/printer-applet-printers.ui
%{_datadir}/apps/printer-applet/printer-applet.notifyrc
%attr(755,root,root) %{_datadir}/apps/printer-applet/printer-applet.py
%{_datadir}/apps/printer-applet/printer-applet.ui
%{_datadir}/apps/printer-applet/printer-appletui.rc
%{_datadir}/apps/printer-applet/statereason.py
%{_datadir}/autostart/printer-applet.desktop
