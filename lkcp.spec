Summary:	Live Kernel Configuration Panel
Summary(pl.UTF-8):	Live Kernel Configuration Panel - panel do konfiguracji jądra w czasie pracy
Name:		lkcp
Version:	0.5.4
Release:	1
License:	GPL v2
Group:		Applications
Source0:	https://webspace.utexas.edu/~hyoussef/%{name}-%{version}.tar.gz
# Source0-md5:	9c630b1cf338761cf93c116943bfc7e9
Patch0:		%{name}-ncurses.patch
URL:		http://webspace.utexas.edu/~hyoussef/
BuildRequires:	glib-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Live Kernel Configuration Panel (LKCP) is an ncurses interface to the
run-time Linux kernel configuration data that can be accessed through
the /proc filesystem. It also generates a bash script of your recently
committed changes to the /proc/sys filesystem.

%description -l pl.UTF-8
Live Kernel Configuration Panel (LKCP) to oparty na ncurses interfejs
do konfiguracji jądra systemu Linux w trakcie pracy (za pomocą systemu
plików /proc). Program ten generuje także skrypt w bashu zawierający
ostatnie zmiany dokonane w systemie plików /proc/sys.

%prep
%setup -q
%patch0 -p1

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
%doc AUTHORS Changelog README TODO Documentation/
%attr(755,root,root) %{_bindir}/*
