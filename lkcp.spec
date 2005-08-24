Summary:	Live Kernel Configuration Panel
Summary(pl):	Live Kernel Configuration Panel - panel do konfiguracji j±dra w czasie pracy
Name:		lkcp
Version:	0.5.3
Release:	1
License:	GPL v2
Group:		Applications
#Source0:	http://webspace.utexas.edu/hyoussef/www/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	020f788b8c9ac52636b357e8929f7e30
URL:		http://webspace.utexas.edu/~hyoussef/
BuildRequires:	glib-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Live Kernel Configuration Panel (LKCP) is an ncurses interface to the
run-time Linux kernel configuration data that can be accessed through
the /proc filesystem. It also generates a bash script of your recently
committed changes to the /proc/sys filesystem.

%description -l pl
Live Kernel Configuration Panel (LKCP) to oparty na ncurses interfejs
do konfiguracji j±dra systemu Linux w trakcie pracy (za pomoc± systemu
plików /proc). Program ten generuje tak¿e skrypt w bashu zawieraj±cy
ostatnie zmiany dokonane w systemie plików /proc/sys.

%prep
%setup -q

%build
%{__make} -C src \
	RESET=true \
	CC="%{__cc}" \
	FLAGS="%{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install src/lkcp $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS Changelog README TODO Documentation/
%attr(755,root,root) %{_bindir}/*
