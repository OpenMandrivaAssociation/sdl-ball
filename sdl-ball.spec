%define uname	SDL-Ball

Name:		sdl-ball
Version:	1.04
Release:	1
Summary:	A Free/OpenSource brick-breaking game with pretty graphics
License:	GPLv3
Group:		Games/Arcade
Url:		http://dustedgames.blogspot.co.uk/p/sdl-ball_20.html
Source0:	http://downloads.sourceforge.net/%{name}/%{version}/%{uname}_%{version}_src.tar.xz
Source1:	%{name}.sh
BuildRequires:	dos2unix
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	pkgconfig(sdl)
BuildRequires:  pkgconfig(opengl)

%description
SDL-Ball is a Free/OpenSource brick-breaking game with pretty graphics.
It is written in C++ using SDL and OpenGL.

Your mission: To smash your way through a series of progressively harder
and more tricky levels. Your tools: Ultrakinetic titanium balls and your
trusty Gruntmazter-3000-Paddle edition.

Features:
* 50 levels.
* OpenGL eye candy. (Nice graphics, really)
* Lots of powerups and powerdowns.
* Powerup Shop - You get special coins for collecting powerups,
  you can spend them on more powerups.
* Highscores.
* Sound.
* Easy to use level editor.
* Themes - Selectable from options menu.
  Themes support loading new gfx,snd and levels.
  A theme can be partial, if a file is missing,
  it will be loaded from the default theme.
  You can even mix between gfx,snd and level themes!
* Controllable with Mouse/Keyboard/Joystick and WiiMote.
* Save and Load games
* Cool Introscreen
* Screenshot function

%prep
%setup -qn %{uname}_src

# Convert to unix line end
find . -name "*.cpp" -exec dos2unix "{}" "+"

%build
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{ldflags}"
%make_build STRIP=/bin/true

%install
# install wrapper
install -Dm 0755 %{S:1} %{buildroot}%{_gamesbindir}/%{name}

# install executable
install -Dm 0755 %{name} %{buildroot}%{_libexecdir}/%{name}/%{name}

# install directories
mkdir -p %{buildroot}%{_libexecdir}/%{name}/themes/{default,dio-sound-theme}
for d in default dio-sound-theme ; do
    cp -a themes/$d %{buildroot}%{_libexecdir}/%{name}/themes/
done

# install icon
install -Dm 0644 themes/default/icon32.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# install Desktop file
install -Dm 0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

# install Appdata file
install -Dm 0644 %{name}.appdata.xml %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%doc changelog.txt README
%license LICENSE.txt
%{_gamesbindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_libexecdir}/%{name}
