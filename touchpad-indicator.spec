Summary:	An indicator to show the status of the touchpad
Name:		touchpad-indicator
Version:	0.7.6.2
Release:	1
License:	GPLv3
Group:		System/Configuration/Hardware
Url:		http://launchpad.net/touchpad-indicator/
Source0:	http://launchpad.net/touchpad-indicator/0.7/0.7.6.2/+download/%{name}_%{version}.orig.tar.xz

Requires:	pyusb
Requires:	gnome-python-gconf

%description
An indicator to show the status of the touchpad, and to enable and disable the 
touchpad.

%prep
%setup -qcn %{name}_%{version}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/applications
mkdir -p %{buildroot}/%{_datadir}/pixmaps
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/scalable/status
mkdir -p %{buildroot}/%{_datadir}/touchpad-indicator
mkdir -p %{buildroot}/%{_datadir}/touchpad-indicator/img

cp img/touchpad-indicator.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
cp img/touchpad-indicator-disabled.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/status/
cp img/touchpad-indicator.svg %{buildroot}/%{_datadir}/pixmaps/
cp img/touchpad-indicator.svg %{buildroot}/%{_datadir}/touchpad-indicator/img
cp touchpad-indicator-autostart.desktop %{buildroot}/%{_datadir}/touchpad-indicator/
cp Touchpad-Indicator.desktop %{buildroot}/%{_datadir}/applications/

mkdir -p %{buildroot}/%{_datadir}/touchpad-indicator
mkdir -p %{buildroot}/%{_datadir}/touchpad-indicator/pyudev
mkdir -p %{buildroot}/%{_datadir}/touchpad-indicator/img
cp *.py %{buildroot}/%{_datadir}/touchpad-indicator/
cp pyudev/*.py %{buildroot}/%{_datadir}/touchpad-indicator/pyudev/

%files
%{_datadir}/touchpad-indicator/%{name}*.desktop
%{_datadir}/touchpad-indicator/*.py
%{_datadir}/touchpad-indicator/pyudev/*.py
%{_datadir}/touchpad-indicator/img/*.svg
%{_datadir}/applications/Touchpad-Indicator.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_iconsdir}/hicolor/scalable/status/*.svg
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg

