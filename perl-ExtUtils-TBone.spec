%include	/usr/lib/rpm/macros.perl
Summary:	ExtUtils-TBone perl module
Summary(pl):	Modu³ perla ExtUtils-TBone
Name:		perl-ExtUtils-TBone
Version:	1.121
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/ExtUtils/ExtUtils-TBone-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils-TBone - a "skeleton" for writing "t/*.t" test files.

%description -l pl
ExtUtils-TBone - "szkielet" dla tworzenia plików testowych "t/*.t".

%prep
%setup -q -n ExtUtils-TBone-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/ExtUtils/TBone.pm
%{_mandir}/man3/*
