Summary:	Settings manager for the Xfce desktop environment
Summary(pl.UTF-8):	Menadżer ustawień dla środowiska Xfce
Name:		xfce4-settings
Version:	4.7.4
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce/4.8pre1/src/%{name}-%{version}.tar.bz2
# Source0-md5:	8ef68534a931c902c714cd251a7485be
Patch0:		%{name}-default-icon-theme.patch
URL:		http://www.xfce.org/projects/xfce4-settings/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.34
BuildRequires:	exo-devel >= 0.3.100
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.12.0
#BuildRequires:	libxfce4util-devel >= %{version}
#BuildRequires:	libxfce4ui-devel >= %{version}
BuildRequires:	libxfce4util-devel >= 4.7.0
BuildRequires:	libxfce4ui-devel >= 4.7.0
BuildRequires:	libxklavier-devel
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.7.0
#BuildRequires:	xfconf-devel >= %{version}
BuildRequires:	xfconf-devel >= 4.7.0
#Requires:	xfconf >= %{version}
Requires:	xfconf >= 4.7.0
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

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/xfce4-accessibility-settings
%attr(755,root,root) %{_bindir}/xfce4-appearance-settings
%attr(755,root,root) %{_bindir}/xfce4-display-settings
%attr(755,root,root) %{_bindir}/xfce4-keyboard-settings
%attr(755,root,root) %{_bindir}/xfce4-mouse-settings
%attr(755,root,root) %{_bindir}/xfce4-settings-editor
%attr(755,root,root) %{_bindir}/xfce4-settings-helper
%attr(755,root,root) %{_bindir}/xfce4-settings-manager
%attr(755,root,root) %{_bindir}/xfsettingsd
%{_sysconfdir}/xdg/autostart/xfce4-settings-helper-autostart.desktop
%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
%{_desktopdir}/xfce-display-settings.desktop
%{_desktopdir}/xfce-keyboard-settings.desktop
%{_desktopdir}/xfce-mouse-settings.desktop
%{_desktopdir}/xfce-settings-manager.desktop
%{_desktopdir}/xfce-ui-settings.desktop
%{_desktopdir}/xfce4-accessibility-settings.desktop
%{_desktopdir}/xfce4-settings-editor.desktop
