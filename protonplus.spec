Name:           protonplus
Version:        0.6.8
Release:        1
Summary:        Simple and powerful manager for Wine, Proton, DXVK and VKD3D
Group:        Graphical desktop/GNOME
License:        GPL-3.0-or-later
URL:            https://github.com/Vysp3r/ProtonPlus
Source0:        https://github.com/Vysp3r/ProtonPlus/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	meson

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  chrpath
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(sdl3)
BuildRequires:	pkgconfig(appstream)

Requires: glib-networking
Requires: gtk4

%description
protonplus is a simple and powerful manager for:
 - Wine
 - Proton
 - DXVK
 - VKD3D
 - Several other runners

Supports Steam, Lutris, Heroic and Bottles.

%prep
%autosetup -n ProtonPlus-%{version} -p1

%install -a
chrpath -d %{buildroot}%{_bindir}/protonplus || :

%find_lang com.vysp3r.ProtonPlus

%files -f com.vysp3r.ProtonPlus.lang
%license LICENSE.md
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md
# install symlink prontonplus -> com.vysp3r.ProtonPlus
%{_bindir}/*
%{_datadir}/applications/com.vysp3r.ProtonPlus.desktop
%{_datadir}/glib-2.0/schemas/com.vysp3r.ProtonPlus.gschema.xml
%{_datadir}/metainfo/com.vysp3r.ProtonPlus.metainfo.xml
%{_iconsdir}/hicolor/*x*/apps/com.vysp3r.ProtonPlus.png
