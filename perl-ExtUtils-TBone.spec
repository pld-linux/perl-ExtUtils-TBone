#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	ExtUtils
%define		pnam	TBone
Summary:	ExtUtils::TBone - a "skeleton" for writing test files
Summary(pl.UTF-8):	ExtUtils::TBone - szkielet do tworzenia testów
Name:		perl-ExtUtils-TBone
Version:	1.124
Release:	9
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	81914cadf266f6cd2083bd321c1557cd
URL:		http://search.cpan.org/dist/ExtUtils-TBone/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::TBone Perl module is intended for folks who release CPAN
modules with "t/*.t" tests. It makes it easy for you to output
syntactically correct test-output while at the same time logging all
test activity to a log file. Hopefully, bug reports which include the
contents of this file will be easier for you to investigate.

%description -l pl.UTF-8
Moduł Perla ExtUtils::TBone jest przeznaczony dla autorów modułów CPAN
zawierających testy "t/*.t". Upraszcza on tworzenie poprawnego
składniowo wyjścia testów, przy jednoczesnym logowaniu wszelkiej
aktywności danego testu. Raporty o błędach zawierające ten log powinny
być łatwiejsze do zbadania.

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
