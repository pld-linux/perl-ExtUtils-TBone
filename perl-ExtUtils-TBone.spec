%include	/usr/lib/rpm/macros.perl
Summary:	ExtUtils-TBone perl module
Summary(pl):	Modu� perla ExtUtils-TBone
Name:		perl-ExtUtils-TBone
Version:	1.117
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/ExtUtils/ExtUtils-TBone-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils-TBone - a "skeleton" for writing "t/*.t" test files.

%description -l pl
ExtUtils-TBone - "szkielet" dla tworzenia plik�w testowych "t/*.t".

%prep
%setup -q -n ExtUtils-TBone-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/ExtUtils/TBone
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv -f .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/ExtUtils/TBone.pm
%{perl_sitearch}/auto/ExtUtils/TBone

%{_mandir}/man3/*
