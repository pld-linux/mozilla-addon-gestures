Summary:	Mouse Gestures
Summary(pl):	Obs³uga gestów
Name:		mozilla-addon-gestures
%define		_realname	mozgest
Version:	0.3.4
%define	fver	%(echo %{version} | tr . _)
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://optimoz.mozdev.org/gestures/%{_realname}_%{fver}.xpi
Source1:	%{_realname}-installed-chrome.txt
URL:		http://optimoz.mozdev.org/gestures/
BuildRequires:	unzip
Requires:	mozilla >= 1.0
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _chromedir      %{_libdir}/mozilla/chrome

%description
Gestures support for Mozilla.

%description -l pl
Obs³uga gestów dla Mozilli.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_chromedir}
cat %{_realname}-installed-chrome.txt >> installed-chrome.txt

%postun
cd %{_chromedir}
cat installed-chrome.txt | grep -v "mozgest" > installed-chrome.txt.tmp
cat installed-chrome.txt.tmp > installed-chrome.txt
rm -f installed-chrome.txt.tmp

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}
%{_chromedir}/%{_realname}-installed-chrome.txt
