Name:           protonplus
Version:        0.6.8
Release:        1
Summary:        Simple and powerful manager for Wine, Proton, DXVK and VKD3D
Group:        Graphical desktop/GNOME
License:        GPL-3.0-or-later
URL:            https://github.com/Vysp3r/ProtonPlus
# Upstream tags are v-prefixed (v0.6.8); a bare version tag 404s.
%global tag v%{version}
Source0:        https://github.com/Vysp3r/ProtonPlus/archive/%{tag}/ProtonPlus-%{version}.tar.gz

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

%build
%meson
%meson_build

%install
%meson_install
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

%changelog
* Sun Sep 20 2026 lshyrilser1 <128003623+lshyrilser1@users.noreply.github.com> - 0.6.8-1
- Update to 0.6.8 (fixes and translation updates upstream)
- Fix Source0 to use the v-prefixed tag (bare version 404s)
