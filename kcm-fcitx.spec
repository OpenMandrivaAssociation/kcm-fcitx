Summary: KCM (Systemsettings) module for configuring fcitx
Name: kcm-fcitx
Version: 0.5.5
Release: 4
URL: http://fcitx-im.org/
License: GPLv2
Source0: http://download.fcitx-im.org/kcm-fcitx/%{name}-%{version}.tar.xz
Group: System/Internationalization
BuildRequires: pkgconfig(fcitx) 
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: cmake(FcitxQt5DBusAddons)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5NewStuff)

%description
KCM (Systemsettings) module for configuring fcitx.

%prep
%autosetup -p1
%global optflags %optflags -Wno-c++11-narrowing

%cmake_kde5

%build
%ninja -j1 -C build

%install
%ninja_install -C build

%find_lang kcm_fcitx

%files -f kcm_fcitx.lang
%{_sysconfdir}/xdg/fcitx-skin.knsrc
%{_libdir}/qt5/plugins/kcm_fcitx.so
%{_datadir}/kservices5/*.desktop
%{_bindir}/kbd-layout-viewer
