Summary:	Mouse Gestures
Summary(pl):	Obs³uga gestów
Name:		mozilla-addon-gestures
%define		_realname	mozgest
Version:	0.3.4
%define	fver	%(echo %{version} | tr . _)
Release:	4
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://optimoz.mozdev.org/gestures/%{_realname}_%{fver}.xpi
# Source0-md5:	2754cac576afa78797c858104fe6cd40
Source1:	%{_realname}-installed-chrome.txt
Source3:	http://surfmind.com/mozgest/optimoz_poster.jpg
# Source3-md5:	a3ae558152b3de63db94b8a7ff740948
Patch0:		mozgest-polish.patch
URL:		http://optimoz.mozdev.org/gestures/
BuildRequires:	unzip
BuildRequires:	zip
Requires(post,postun):	textutils
Requires:	mozilla >= 1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define         _chromedir      %{_datadir}/mozilla/chrome

%description
Gestures support for Mozilla.

%description -l pl
Obs³uga gestów dla Mozilli.

%prep
%setup -q -c %{name}-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

cd %{_realname}
zip -r -9 -m ../%{_realname}.jar ./
cd -
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE3} .
install %{_realname}.jar $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%doc optimoz_poster.jpg
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
