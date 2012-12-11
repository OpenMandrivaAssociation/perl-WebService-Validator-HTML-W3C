%define upstream_name    WebService-Validator-HTML-W3C
%define upstream_version 0.26

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Warning messages from the W3Cs online Validator
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WebService/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(LWP)
BuildRequires:	perl(XML::XPath)
BuildArch:	noarch

%description
WebService::Validator::HTML::W3C provides access to the W3C's online Markup
validator. As well as reporting on whether a page is valid it also provides
access to a detailed list of the errors and where in the validated document
they occur.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.260.0-2mdv2011.0
+ Revision: 658423
- rebuild for updated rpm-setup

* Wed Sep 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.260.0-1mdv2010.0
+ Revision: 435703
- update to 0.26

* Fri Jul 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.250.0-1mdv2010.0
+ Revision: 399259
- update to 0.25

* Sat May 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.240.0-1mdv2010.0
+ Revision: 381445
- adding missing buildrequires:
- import perl-WebService-Validator-HTML-W3C


* Sat May 30 2009 cpan2dist 0.24-1mdv
- initial mdv release, generated with cpan2dist

