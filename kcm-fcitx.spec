Summary: KCM (Systemsettings) module for configuring fcitx
Name: kcm-fcitx
Version: 0.5.3
Release: 1
URL: http://fcitx-im.org/
License: GPLv2
Source0: http://download.fcitx-im.org/kcm-fcitx/%{name}-%{version}.tar.xz
Group: System/Internationalization
BuildRequires: pkgconfig(fcitx) 
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5NewStuff)

%track
prog %{name} = {
	url = http://code.google.com/p/fcitx/downloads/list
	regex = %name-(__VER__)\.tar\.xz
	version = %{version}
}

%description
KCM (Systemsettings) module for configuring fcitx.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kcm_fcitx

%files -f kcm_fcitx.lang

