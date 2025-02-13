%define		xfce_version	4.20.0
Summary:	Settings manager for the Xfce desktop environment
Summary(pl.UTF-8):	Menadżer ustawień dla środowiska Xfce
Name:		xfce4-settings
Version:	4.20.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/xfce/xfce4-settings/4.20/%{name}-%{version}.tar.bz2
# Source0-md5:	f6a275e5e7c30dcceb4daa480375f8d0
URL:		https://www.xfce.org/projects/xfce4-settings/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	colord-devel >= 1.0.2
BuildRequires:	dbus-glib-devel >= 0.84
BuildRequires:	exo-devel >= 4.15.1
BuildRequires:	fontconfig-devel >= 2.6.0
BuildRequires:	garcon-devel >= 0.1.10
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.72.0
BuildRequires:	gtk+3-devel >= 3.24.0
BuildRequires:	intltool
BuildRequires:	libcanberra-devel
BuildRequires:	libinput-devel
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.20.0
BuildRequires:	libxfce4util-devel >= %{xfce_version}
BuildRequires:	libxklavier-devel
BuildRequires:	pkgconfig
BuildRequires:	upower-devel
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
BuildRequires:	xfconf-devel >= 4.20.0
BuildRequires:	xorg-driver-input-libinput-devel
BuildRequires:	xorg-lib-libXcursor-devel >= 1.1.0
BuildRequires:	xorg-lib-libXi-devel >= 1.2.0
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-proto-inputproto-devel >= 1.4.0
Requires:	xfconf >= %{xfce_version}
Obsoletes:	xfce-mcs-manager < 4.16
Obsoletes:	xfce-mcs-plugins < 4.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The settings manager allows you to customize your Xfce desktop
environment in an easy and intuitive way.

%description -l pl.UTF-8
Menadżer ustawień pozwala w łatwy i intuicyjny sposób dostosowywać
środowisko Xfce.

%prep
%setup -q
%{__sed} -i '1s,/usr/bin/env python3$,%{__python3},' \
                dialogs/mime-settings/helpers/xfce4-compose-mail

mkdir -p m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-sound-settings \
	--enable-upower-glib

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/modules/libxfsettingsd-gtk-settings-sync.la

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hye,ie,ur_PK}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/xfce4-accessibility-settings
%attr(755,root,root) %{_bindir}/xfce4-appearance-settings
%attr(755,root,root) %{_bindir}/xfce4-color-settings
%attr(755,root,root) %{_bindir}/xfce4-display-settings
%attr(755,root,root) %{_bindir}/xfce4-find-cursor
%attr(755,root,root) %{_bindir}/xfce4-keyboard-settings
%attr(755,root,root) %{_bindir}/xfce4-mime-helper
%attr(755,root,root) %{_bindir}/xfce4-mime-settings
%attr(755,root,root) %{_bindir}/xfce4-mouse-settings
%attr(755,root,root) %{_bindir}/xfce4-settings-editor
%attr(755,root,root) %{_bindir}/xfce4-settings-manager
%attr(755,root,root) %{_bindir}/xfsettingsd
%attr(755,root,root) %{_libdir}/gtk-3.0/modules/libxfsettingsd-gtk-settings-sync.so
%dir %{_libdir}/xfce4/settings
%attr(755,root,root) %{_libdir}/xfce4/settings/appearance-install-theme
%attr(755,root,root) %{_libdir}/xfce4/xfce4-compose-mail
%{_sysconfdir}/xdg/autostart/xfsettingsd.desktop
%{_sysconfdir}/xdg/menus/xfce-settings-manager.menu
%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
%{_sysconfdir}/xdg/xfce4/helpers.rc
%{_desktopdir}/xfce-display-settings.desktop
%{_desktopdir}/xfce-keyboard-settings.desktop
%{_desktopdir}/xfce-mouse-settings.desktop
%{_desktopdir}/xfce-settings-manager.desktop
%{_desktopdir}/xfce-ui-settings.desktop
%{_desktopdir}/xfce4-accessibility-settings.desktop
%{_desktopdir}/xfce4-color-settings.desktop
%{_desktopdir}/xfce4-file-manager.desktop
%{_desktopdir}/xfce4-mail-reader.desktop
%{_desktopdir}/xfce4-mime-settings.desktop
%{_desktopdir}/xfce4-settings-editor.desktop
%{_desktopdir}/xfce4-terminal-emulator.desktop
%{_desktopdir}/xfce4-web-browser.desktop
%dir %{_datadir}/xfce4/helpers
%{_datadir}/xfce4/helpers/*.desktop
%{_iconsdir}/hicolor/*x*/apps/*.png
%{_iconsdir}/hicolor/*x*/devices/xfce-display-*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_iconsdir}/hicolor/scalable/devices/*.svg
