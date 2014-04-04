%define rcN rc4

Summary:	Free/OpenSource brick-breaking game with pretty graphics
Name:		sdl-ball
Version:	1.01
Release:	3
License:	GPLv2+
Group:		Games/Arcade
Url:		http://sdl-ball.sourceforge.net/
Source0:	http://dl.sourceforge.net/sourceforge/%name/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(gimp-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_ttf)

%description
SDL-Ball is a Free/OpenSource brick-breaking game for Linux,
BSD and windows with pretty graphics. It is written in C++ using
SDL and OpenGL, here is the project page on sf.net.

Your mission: To smash your way through a series of progressively
harder and more tricky levels.
Your tools: Ultrakinetic titanium balls and your
trusty Gruntmazter-3000-Paddle edition.

%files
%doc README changelog.txt
%{_gamesbindir}/%{name}
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*
%{_iconsdir}/*.png
%{_datadir}/applications/%{name}.desktop

#----------------------------------------------------------------------------

%package leveleditor
Summary:	Level editor for SDL-Ball
Group:		Games/Arcade

%description leveleditor
SDL-Ball is a Free/OpenSource brick-breaking game with pretty graphics.

This package includes a level editor for SDL-Ball (GIMP plugin).

Start gimp from a terminal in order to record the output from
the plugin (you need that).

%files leveleditor
%{_libdir}/gimp/2.0/plug-ins/*

#----------------------------------------------------------------------------


%prep
%setup -q -n %{name}
# clean sources
rm -f *.o sdl-ball
sed -i '18i#include <unistd.h>' input.cpp

%build
%setup_compile_flags
%make DATADIR=%{_gamesdatadir}/%{name}/
pushd leveleditor/gimp-leveleditor
gimptool-2.0 --build gimp-sdlball.c

%install
mkdir -p %{buildroot}%{_gamesdatadir} %{buildroot}%{_gamesbindir}
mkdir -p %{buildroot}%{_libdir}/gimp/2.0/plug-ins
install %{name} %{buildroot}%{_gamesbindir}
install leveleditor/gimp-leveleditor/gimp-sdlball %{buildroot}%{_libdir}/gimp/2.0/plug-ins
cp -a themes %{buildroot}%{_gamesdatadir}/%{name}

mkdir -p %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=SDL-Ball
Exec=sdl-ball
Icon=sdl-ball
GenericName=Breakout Game
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

mkdir -p %{buildroot}%{_iconsdir}
cp themes/default/icon32.png %{buildroot}%{_iconsdir}/%{name}.png

