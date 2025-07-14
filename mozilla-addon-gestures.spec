%define		_realname	mozgest
%define	fver	%(echo %{version} | tr . _)
Summary:	Mouse Gestures
Summary(pl.UTF-8):	Obsługa gestów
Name:		mozilla-addon-gestures
Version:	0.3.4
Release:	5
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
Requires(post,postun):	mozilla >= 5:1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 2:1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
Gestures support for Mozilla.

%description -l pl.UTF-8
Obsługa gestów dla Mozilli.

%prep
%setup -q -c
%patch -P0 -p1

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
if [ "$1" = 1 ]; then
	%{_sbindir}/mozilla-chrome+xpcom-generate
fi

%postun
[ ! -x %{_sbindir}/mozilla-chrome+xpcom-generate ] || %{_sbindir}/mozilla-chrome+xpcom-generate


%files
%defattr(644,root,root,755)
%doc optimoz_poster.jpg
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
