%define		xfce_version	4.12.0
Summary:	Settings manager for the Xfce desktop environment
Summary(pl.UTF-8):	Menadżer ustawień dla środowiska Xfce
Name:		xfce4-settings
Version:	4.13.6
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/xfce/xfce4-settings/4.13/%{name}-%{version}.tar.bz2
# Source0-md5:	480d3ce2e313cd25e397fdf571d65c42
Patch0:		01_use-tango-icon-theme.patch
URL:		http://www.xfce.org/projects/xfce4-settings/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.84
BuildRequires:	exo-devel >= 0.12.0
BuildRequires:	fontconfig-devel >= 2.6.0
BuildRequires:	garcon-devel >= 0.1.10
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.45.8
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libcanberra-devel
BuildRequires:	libinput-devel
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.13.0
BuildRequires:	libxfce4util-devel >= %{xfce_version}
BuildRequires:	libxklavier-devel
BuildRequires:	pkgconfig
BuildRequires:	upower-devel
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
BuildRequires:	xfconf-devel >= 4.13.0
BuildRequires:	xorg-driver-input-libinput-devel
BuildRequires:	xorg-lib-libXcursor-devel >= 1.1.0
BuildRequires:	xorg-lib-libXi-devel >= 1.2.0
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-proto-inputproto-devel >= 1.4.0
Requires:	xfconf >= %{xfce_version}
Obsoletes:	xfce-mcs-manager
Obsoletes:	xfce-mcs-plugins
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The settings manager allows you to customize your Xfce desktop
environment in an easy and intuitive way.

%description -l pl.UTF-8
Menadżer ustawień pozwala w łatwy i intuicyjny sposób dostosowywać
środowisko Xfce.

%prep
%setup -q
%patch0 -p1

mkdir -p m4

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-pluggable-dialogs \
	--enable-sound-settings

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ie

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/xfce4-accessibility-settings
%attr(755,root,root) %{_bindir}/xfce4-appearance-settings
%attr(755,root,root) %{_bindir}/xfce4-color-settings
%attr(755,root,root) %{_bindir}/xfce4-display-settings
%attr(755,root,root) %{_bindir}/xfce4-find-cursor
%attr(755,root,root) %{_bindir}/xfce4-keyboard-settings
%attr(755,root,root) %{_bindir}/xfce4-mime-settings
%attr(755,root,root) %{_bindir}/xfce4-mouse-settings
%attr(755,root,root) %{_bindir}/xfce4-settings-editor
%attr(755,root,root) %{_bindir}/xfce4-settings-manager
%attr(755,root,root) %{_bindir}/xfsettingsd
%dir %{_libdir}/xfce4/settings
%attr(755,root,root) %{_libdir}/xfce4/settings/appearance-install-theme
%{_sysconfdir}/xdg/autostart/xfsettingsd.desktop
%{_sysconfdir}/xdg/menus/xfce-settings-manager.menu
%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
%{_desktopdir}/xfce-display-settings.desktop
%{_desktopdir}/xfce-keyboard-settings.desktop
%{_desktopdir}/xfce-mouse-settings.desktop
%{_desktopdir}/xfce-settings-manager.desktop
%{_desktopdir}/xfce-ui-settings.desktop
%{_desktopdir}/xfce4-accessibility-settings.desktop
%{_desktopdir}/xfce4-color-settings.desktop
%{_desktopdir}/xfce4-mime-settings.desktop
%{_desktopdir}/xfce4-settings-editor.desktop
%{_iconsdir}/hicolor/*x*/apps/xfce4-color-settings.png
%{_iconsdir}/hicolor/*x*/devices/xfce-display-*.png
%{_iconsdir}/hicolor/scalable/apps/xfce4-color-settings.svg
