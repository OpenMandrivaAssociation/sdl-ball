%define rcN	rc4
Name:	sdl-ball
Version:	1.0
Release: 	%mkrel 1
Summary:	Free/OpenSource brick-breaking game with pretty graphics
Group:	Games/Arcade
License:	GPLv2+
Url:	http://sdl-ball.sourceforge.net/
Source0:	http://dl.sourceforge.net/sourceforge/%name/%name-%version.tar.bz2
#Source1: %name.png
#Source2: %name.desktop
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

# Automatically added by buildreq on Wed Nov 12 2008
BuildRequires: gcc-c++ GL-devel SDL-devel SDL_image-devel SDL_mixer-devel SDL_ttf-devel gimp-devel

%description
SDL-Ball is a Free/OpenSource brick-breaking game for Linux,BSD and windows with pretty graphics. It is written in C++ using SDL and OpenGL, here is the project page on sf.net.

Your mission: To smash your way through a series of progressively harder and more tricky levels. Your tools: Ultrakinetic titanium balls and your trusty Gruntmazter-3000-Paddle edition.

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

%build
%make DATADIR=%_gamesdatadir/%name/
pushd leveleditor/gimp-leveleditor
gimptool-2.0 --build gimp-sdlball.c

%install
rm -rf %{buildroot}

mkdir -p %buildroot%_gamesdatadir %buildroot%_gamesbindir
mkdir -p %buildroot%_libdir/gimp/2.0/plug-ins
install -s %name %buildroot%_gamesbindir
install -s leveleditor/gimp-leveleditor/gimp-sdlball %buildroot%_libdir/gimp/2.0/plug-ins
cp -a themes %buildroot%_gamesdatadir/%name

## TODO: level editor

# below is the desktop file and icon stuff.
##mkdir -p $RPM_BUILD_ROOT%_desktopdir
##desktop-file-install --vendor "" \
##  --dir $RPM_BUILD_ROOT%_desktopdir \
##  #SOURCE2
##mkdir -p $RPM_BUILD_ROOT%_niconsdir
##install -p -m 644 #SOURCE1 \
##  $RPM_BUILD_ROOT%_niconsdir

%clean
rm -rf %{buildroot}

%files
%doc README changelog.txt leveleditor
%_gamesbindir/%name
%dir %_gamesdatadir/%name
%_gamesdatadir/%name/*

%files leveleditor
%doc leveleditor leveleditor/gimp-leveleditor/readme
%_libdir/gimp/2.0/plug-ins/*

