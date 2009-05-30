%define upstream_name    WebService-Validator-HTML-W3C
%define upstream_version 0.24

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Warning messages from the W3Cs online Validator
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/WebService/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Accessor)
BuildRequires: perl(LWP)
BuildRequires: perl(XML::XPath)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
WebService::Validator::HTML::W3C provides access to the W3C's online Markup
validator. As well as reporting on whether a page is valid it also provides
access to a detailed list of the errors and where in the validated document
they occur.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*

