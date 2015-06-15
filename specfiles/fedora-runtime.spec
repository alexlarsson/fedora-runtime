Name:           fedora-runtime
Version:        23
Release:        3%{?dist}
Summary:        An xdg-app runtime based on fedora
Source1:        50-xdg-app.conf
BuildArch:      noarch

License:        GPL

Requires:       fedora-release basesystem glibc nss-altfiles bash setup rpm
Requires:	gnupg2
Requires:	xz gzip bzip2
Requires:	coreutils util-linux which curl findutils btrfs-progs
Requires:       xorg-x11-fonts-Type1
Requires:	abattis-cantarell-fonts urw-fonts
Requires:	dejavu-sans-fonts dejavu-serif-fonts dejavu-lgc-sans-fonts dejavu-lgc-serif-fonts dejavu-sans-mono-fonts dejavu-lgc-sans-mono-fonts
Requires:	gnu-free-serif-fonts gnu-free-mono-fonts gnu-free-sans-fonts google-crosextra-caladea-fonts google-crosextra-carlito-fonts
Requires:	liberation-fonts-common liberation-mono-fonts liberation-narrow-fonts liberation-sans-fonts liberation-serif-fonts
Requires:	libICE libSM libX11 libXScrnSaver libXau libXcomposite libXcursor libXdamage libXext libXfixes libXft libXi libXinerama libXpm libXrandr libXrender libXt libXtst libXv libXxf86vm libxkbcommon-x11 xcb-util libXfont libfontenc
Requires:       xorg-x11-font-utils ttmkfdir
Requires:	mesa-libEGL mesa-libglapi mesa-libgbm mesa-libwayland-egl mesa-libGL mesa-dri-drivers mesa-libGLU libGLEW
Requires:	pulseaudio-libs pulseaudio-libs-glib2
Requires:	gtk2 gtk2-immodules gtk3 gtk3-immodules
Requires:       gstreamer1 gstreamer1-plugins-base gstreamer1-plugins-good
Requires:	clutter clutter-gtk
Requires:	adwaita-icon-theme gnome-themes-standard gsettings-desktop-schemas
Requires:	gvfs-client gobject-introspection dbus-glib dconf gjs json-glib librsvg2 libsecret webkitgtk4 libproxy avahi-gobject
Requires:       enchant aspell
Requires:	lcms2 zenity desktop-file-utils attr bzip2 elfutils less libatomic_ops libtool-ltdl libsamplerate tar zip unzip startup-notification
Requires:	speex libvpx libexif libogg jasper flac-libs libjpeg-turbo libpng libsndfile libtheora libtiff libvisual libvorbis libwebp giflib openjpeg2
Requires:	SDL2 SDL2_image SDL2_net SDL2_mixer SDL2_ttf
Requires:	perl python python3 python3-cairo python3-gobject
Requires:       qt5-qtbase-gui qt5-qtdeclarative qt5-qtlocation qt5-qtsensors qt5-qttools-libs-designer qt5-qtwebkit qt5-qtxmlpatterns
Requires:	qt qt-x11

%description
An xdg-app runtime based on fedora

%prep


%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_prefix}/cache/fontconfig
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
install -t $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d -m 644 %{SOURCE1} 

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/
echo "/app/%{_lib}" > $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/app.conf

%post -p /sbin/ldconfig

%files
%{_prefix}/cache/fontconfig
%{_sysconfdir}/fonts/conf.d/*
%{_sysconfdir}/ld.so.conf.d/app.conf

%changelog
* Wed Jun  3 2015 Alexander Larsson <alexl@redhat.com>
- Initial version
