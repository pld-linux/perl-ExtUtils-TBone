%define	pdir	ExtUtils
%define	pnam	TBone
%include	/usr/lib/rpm/macros.perl
Summary:	ExtUtils-TBone perl module
Summary(pl):	Modu³ perla ExtUtils-TBone
Name:		perl-ExtUtils-TBone
Version:	1.124
Release:	4

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
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
gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs/*
%{perl_sitelib}/ExtUtils/TBone.pm
%{_mandir}/man3/*
