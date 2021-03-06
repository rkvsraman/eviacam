#
# spec file for package eviacam (Version 1.7.0)
#
# Copyright 2008-09 Cesar Mauri <cesar@crea-si.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# SuSE detection
%define is_not_suse %(test ! -e /etc/SuSE-release && echo 1 || echo 0)
# Mandrake detection
#%define is_mandrake %(test -e /etc/mandrake-release && echo 1 || echo 0)

Summary: A Cross-Platform Webcam Based Mouse Emulator
Name: eviacam
Version: 1.7.0
Release: 0
License: GPL
Group: Applications/Accessibility
URL: http://viacam.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Source: %{name}-%{version}.tar.bz2
Packager: Cesar Mauri <cesar@crea-si.com>
Autoreq: 1

Requires: opencv >= 1.0
BuildRequires: opencv-devel
%if %is_not_suse
Requires: libXtst
Requires: libXext
Requires: wxGTK >= 2.6
BuildRequires: wxGTK-devel
%else
Requires: wxWidgets >= 2.6
BuildRequires: wxWidgets-devel
%endif

Provides:  eviacam

%define prefix /usr
# Different distributions expect sources to be in different places;
# the following solves this problem, but makes it harder to reuse .src.rpm
#%define _sourcedir /tmp

#Docdir:    %{prefix}/share/doc

%description
Enable Viacam (aka eViacam) is a mouse replacement software that moves
the pointer as you move your head. It works on standard PCs equipped 
with a web camera. No additional hardware is required. Based on the 
award winning Facial Mouse software.

%description -l es
Enable Viacam (eViacam) es un programa de ordenador que sustituye la 
funcionalidad del ratón permitiendo mover el puntero a partir del movimiento 
de la cabeza. Funciona en un ordenador PC equipado con una cámara web, sin 
elementos adicionales. eViacam está basado en el programa Ratón Facial 
galardonado con varios premios.

%description -l ca
Enable Viacam (eViacam) és un programa d'ordinador que substitueix la 
funcionalitat del ratolí permetent moure el punter a partir del moviment del cap.
Funciona en un ordinador PC equipat amb una càmera web, sense elements 
addicionals. eViacam està basat en el programa Ratón Facial guardonat amb 
diversos premis. 

%description -l gl
Enable Viacam (eViacam) é un programa de computador que substitúe a 
funcionalidade do rato permitindo mover o punteiro a partir do movemento da 
cabeza. Funciona nun ordenador PC equipado cunha cámara web, sen elementos 
adicionais. eViacam está baseado no programa Rato Facial galardoado con 
varios premios.

%prep

%setup 

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure --disable-rpath --prefix=%{prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT prefix=%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog COPYING INSTALL README THANKS TODO
%{prefix}/bin/*
%{prefix}/share/*

%define date%(echo `LC_ALL="C" date +"%a %b %d %Y"`)
%changelog
* %{date} César Mauri <cesar@crea-si.com>
  - Auto building %{version}-%{release}
* Fri May 1 2009 César Mauri <cesar@crea-si.com>
  - First package release
