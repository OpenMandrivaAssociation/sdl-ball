%define rcN	rc4
Name:	sdl-ball
Version:	1.01
Release: 2
Summary:	Free/OpenSource brick-breaking game with pretty graphics
Group:	Games/Arcade
License:	GPLv2+
Url:	http://sdl-ball.sourceforge.net/
Source0:	http://dl.sourceforge.net/sourceforge/%name/%name-%version.tar.bz2
BuildRequires: gcc-c++ 
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(sdl)
BuildRequires: pkgconfig(SDL_image)
BuildRequires: pkgconfig(SDL_mixer)
BuildRequires: pkgconfig(SDL_ttf)
BuildRequires: pkgconfig(gimp-2.0)


%description
SDL-Ball is a Free/OpenSource brick-breaking game for Linux,
BSD and windows with pretty graphics. It is written in C++ using 
SDL and OpenGL, here is the project page on sf.net.

Your mission: To smash your way through a series of progressively 
harder and more tricky levels. 
Your tools: Ultrakinetic titanium balls and your 
trusty Gruntmazter-3000-Paddle edition.

%package leveleditor
Group: Games/Arcade
Summary: Two level editora for SDL-Ball

%description leveleditor
SDL-Ball is a Free/OpenSource brick-breaking game with pretty graphics.

This package includes two level editors for SDL-Ball, 
JavaScript-based (see %_defaultdocdir/%name-%version/index.html) and GIMP plugin.
Start gimp from a terminal in order to record the output from the plugin (you need that)



%prep
%setup -q -n %name
# clean sources
rm -f *.o sdl-ball
sed -i '18i#include <unistd.h>' input.cpp

%build
%setup_compile_flags
%make DATADIR=%_gamesdatadir/%name/
pushd leveleditor/gimp-leveleditor
gimptool-2.0 --build gimp-sdlball.c

%install
mkdir -p %buildroot%_gamesdatadir %buildroot%_gamesbindir
mkdir -p %buildroot%_libdir/gimp/2.0/plug-ins
install -s %name %buildroot%_gamesbindir
install -s leveleditor/gimp-leveleditor/gimp-sdlball %buildroot%_libdir/gimp/2.0/plug-ins
cp -a themes %buildroot%_gamesdatadir/%name

mkdir -p %buildroot%_datadir/applications
cat << EOF > %buildroot%_datadir/applications/mandriva-%name.desktop
[Desktop Entry]
Name=SDL-Ball
Exec=sdl-ball
Icon=sdl-ball
GenericName=Breakout Game
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

mkdir -p %buildroot%_iconsdir
cp themes/default/icon32.png %buildroot%_iconsdir/%name.png


%files
%doc README changelog.txt leveleditor
%_gamesbindir/%name
%dir %_gamesdatadir/%name
%_gamesdatadir/%name/*
%_iconsdir/*.png
%_datadir/applications/mandriva-%name.desktop

%files leveleditor
%doc leveleditor leveleditor/gimp-leveleditor/readme
%_libdir/gimp/2.0/plug-ins/*


%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.01-2mdv2011.0
+ Revision: 614830
- the mass rebuild of 2010.1 packages

* Wed Dec 16 2009 Jérôme Brenier <incubusss@mandriva.org> 1.01-1mdv2010.1
+ Revision: 479140
- clean sources before building
- new version 1.01

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2010.0
+ Revision: 445092
- rebuild

* Sun Apr 05 2009 Funda Wang <fwang@mandriva.org> 1.0-2mdv2009.1
+ Revision: 364157
- add desktop file
- use flags

* Sun Jan 11 2009 Zombie Ryushu <ryushu@mandriva.org> 1.0-1mdv2009.1
+ Revision: 328327
- First Mandriva version
- import sdl-ball


* Wed Nov 12 2008 Fr. Br. George <george@altlinux.ru> 0.13-alt1
- Version up

* Thu Oct 30 2008 Fr. Br. George <george@altlinux.ru> 0.12-alt1
- Initial build from scratch

