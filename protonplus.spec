Name:           protonplus
Version:        0.4.20
Release:        1
Summary:        Simple and powerful manager for Wine, Proton, DXVK and VKD3D
License:        GPL-3.0-or-later
URL:            https://github.com/Vysp3r/ProtonPlus
Source0:        https://github.com/Vysp3r/ProtonPlus/archive/%{version}/ProtonPlus-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  appstream-util
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libsoup-3.0)

Requires:       glib-networking

%description
%{repo} is a simple and powerful manager for:
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

%find_lang com.vysp3r.ProtonPlus

# create symlink prontonplus -> com.vysp3r.ProtonPlus
%{__ln_s} %{_bindir}/%{flatpak_name} %{buildroot}%{_bindir}/%{name}

%files -f com.vysp3r.ProtonPlus.lang
%license LICENSE.md
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md
# install symlink prontonplus -> com.vysp3r.ProtonPlus
%{_bindir}/%{name}
