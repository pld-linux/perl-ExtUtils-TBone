%include	/usr/lib/rpm/macros.perl
%define	pdir	ExtUtils
%define	pnam	TBone
Summary:	ExtUtils::TBone perl module
Summary(pl):	Modu³ perla ExtUtils::TBone
Name:		perl-ExtUtils-TBone
Version:	1.124
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::TBone - a "skeleton" for writing "t/*.t" test files.

%description -l pl
ExtUtils::TBone - "szkielet" dla tworzenia plików testowych "t/*.t".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/*
%{perl_vendorlib}/ExtUtils/TBone.pm
%{_mandir}/man3/*
