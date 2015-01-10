%define beta %{nil}
%define scmrev %{nil}

Name: kcm-fcitx
Version: 0.4.3
%if "%{beta}" == ""
%if "%{scmrev}" == ""
Release: 8
Source0: http://download.fcitx-im.org/kcm-fcitx/%{name}-%{version}.tar.xz
%else
Release: 0.%{scmrev}.1
Source0: %{name}-%{scmrev}.tar.xz
%endif
%else
%if "%{scmrev}" == ""
Release: 0.%{beta}.1
Source0: %{name}-%{version}%{beta}.tar.bz2
%else
Release: 0.%{beta}.0.%{scmrev}.1
Source0: %{name}-%{scmrev}.tar.xz
%endif
%endif
Summary: KCM (Systemsettings) module for configuring fcitx
URL: http://fcitx-im.org/
License: GPLv2
Group: System/Internationalization
BuildRequires: pkgconfig(fcitx) 
BuildRequires: pkgconfig(fcitx-qt) 
BuildRequires: kdelibs4-devel
BuildRequires: pkgconfig(xkbfile)
BuildRequires: fcitx-qt4
BuildRequires: pkgconfig(qimageblitz)

%track
prog %{name} = {
	url = http://code.google.com/p/fcitx/downloads/list
	regex = %name-(__VER__)\.tar\.xz
	version = %{version}
}

%description
KCM (Systemsettings) module for configuring fcitx

%prep
%if "%{scmrev}" == ""
%setup -q -n %{name}-%{version}%{beta}
%else
%setup -q -n %{name}
%endif

%build
%cmake
%make

%install
%makeinstall_std -C build
%find_lang kcm_fcitx

%files -f kcm_fcitx.lang
%_bindir/kbd-layout-viewer
%_libdir/kde4/kcm_fcitx.so
%_datadir/applications/kde4/kbd-layout-viewer.desktop
%_datadir/config/fcitx-skin.knsrc
%_datadir/kde4/services/kcm_fcitx.desktop
