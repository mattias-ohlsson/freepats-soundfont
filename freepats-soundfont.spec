Name:           freepats-soundfont
Version:        20191001
Release:        1%{?dist}
Summary:        General MIDI SFZ/SF2 sound set

License:        GPLv3+ with exceptions
URL:            https://freepats.zenvoid.org/SoundSets/general-midi.html
Source0:        https://freepats.zenvoid.org/SoundSets/FreePats-GeneralMIDI/FreePatsGM-SF2-%{version}.tar.xz
Source1:        https://freepats.zenvoid.org/SoundSets/FreePats-GeneralMIDI/FreePatsGM-SFZ-%{version}.tar.xz
BuildArch:      noarch

%define common_description \
FreePath General MIDI sound set, assembled from scratch. Currently the sound\
set is incomplete and contains 30 entries for the melodic sound set and 19\
entries for the percussion kit.

%description
%common_description

%package gm-sf2
Summary:        General MIDI sound set in SF2 format
 
%description gm-sf2
%common_description
 
This package contains FreePats General MIDI (GM) sound set in SF2 format.

%package gm-sfz
Summary:        General MIDI sound set in SFZ format
 
%description gm-sfz
%common_description
 
This package contains FreePats General MIDI (GM) sound set in SFZ format.

%prep
%setup -c
%setup -c -D -a 1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -p -D FreePatsGM-SF2-%{version}/FreePatsGM-%{version}.sf2 $RPM_BUILD_ROOT%{_datadir}/soundfonts/FreePats-GM.sf2
install --directory $RPM_BUILD_ROOT%{_datadir}/soundfonts/freepats-gm/
cp -a FreePatsGM-SFZ-%{version}/*.sfz $RPM_BUILD_ROOT%{_datadir}/soundfonts/freepats-gm/
cp -a FreePatsGM-SFZ-%{version}/samples $RPM_BUILD_ROOT%{_datadir}/soundfonts/freepats-gm/

%files gm-sf2
%license FreePatsGM-SF2-%{version}/gpl.txt
%doc FreePatsGM-SF2-%{version}/readme.txt
%{_datadir}/soundfonts/FreePats-GM.sf2

%files gm-sfz
%license FreePatsGM-SFZ-%{version}/gpl.txt
%doc FreePatsGM-SFZ-%{version}/readme.txt
%{_datadir}/soundfonts/freepats-gm

%changelog
* Fri Jan 24 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 20191001-1
- Initial build
