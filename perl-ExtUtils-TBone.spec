#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	ExtUtils
%define	pnam	TBone
Summary:	ExtUtils::TBone - a "skeleton" for writing test files
Summary(pl):	ExtUtils::TBone - szkielet do tworzenia testów
Name:		perl-ExtUtils-TBone
Version:	1.124
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	81914cadf266f6cd2083bd321c1557cd
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::TBone Perl module is intended for folks who release CPAN
modules with "t/*.t" tests. It makes it easy for you to output
syntactically correct test-output while at the same time logging all
test activity to a log file. Hopefully, bug reports which include the
contents of this file will be easier for you to investigate.

%description -l pl
Modu³ Perla ExtUtils::TBone jest przeznaczony dla autorów modu³ów CPAN
zawieraj±cych testy "t/*.t". Upraszcza on tworzenie poprawnego
sk³adniowo wyj¶cia testów, przy jednoczesnym logowaniu wszelkiej
aktywno¶ci danego testu. Raporty o b³êdach zawieraj±ce ten log powinny
byæ ³atwiejsze do zbadania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/*
%{perl_vendorlib}/ExtUtils/TBone.pm
%{_mandir}/man3/*
