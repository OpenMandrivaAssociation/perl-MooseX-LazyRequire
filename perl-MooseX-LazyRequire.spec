%define upstream_name    MooseX-LazyRequire
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Required attributes which fail only when trying to use them
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/MooseX-LazyRequire-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Test::Fatal)
BuildRequires: perl(Test::CheckDeps)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Types::Moose)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More) >= 0.900.0
BuildRequires:	perl(aliased)
BuildRequires:	perl(namespace::autoclean)

BuildArch:	noarch

%description
This module adds a 'lazy_require' option to Moose attribute declarations.

The reader methods for all attributes with that option will throw an
exception unless a value for the attributes was provided earlier by a
constructor parameter or through a writer method.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 654126
- update to new version 0.07

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 561036
- update to 0.06

* Thu Jul 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 553515
- extract runtime requires: from meta.yml

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 552417
- update to 0.05

* Sat Sep 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 438548
- update to 0.04

* Wed Aug 19 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 418127
- update to 0.03

* Sun Aug 16 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 417020
- adding missing buildrequires:
- adding missing buildrequires:
- import perl-MooseX-LazyRequire


* Sun Aug 16 2009 cpan2dist 0.01-1mdv
- initial mdv release, generated with cpan2dist

