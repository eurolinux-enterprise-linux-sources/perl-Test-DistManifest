Name:           perl-Test-DistManifest
Version:        1.012
Release:        4%{?dist}
Summary:        Author test that validates a package MANIFEST
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-DistManifest/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/Test-DistManifest-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(Module::Manifest) >= 0.07
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More) >= 0.62
# Tests only:
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::NoWarnings) >= 0.084
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Module::Manifest) >= 0.07
Requires:       perl(Test::Builder)
# This is a plug-in into Test::More. Depend on it even if not mentioned in the
# code
Requires:       perl(Test::More) >= 0.62

# Filter underspecifed dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\((Module::Manifest|Test::Builder)\\)$

%description
This module provides a simple method of testing that a MANIFEST matches the
distribution.

%prep
%setup -q -n Test-DistManifest-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=perl OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# post-install rpmbuild scripts contaminates RPM_BUILD_ROOT (bug #672538).
rm debug*.list
make test

%files
%doc Changes examples LICENSE README
%{perl_privlib}/*
%{_mandir}/man3/*

%changelog
* Tue Nov 20 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1.012-4
- Remove doubled requires

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.012-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 1.012-2
- Perl 5.16 rebuild

* Mon Apr 23 2012 Petr Pisar <ppisar@redhat.com> - 1.012-1
- 1.012 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.011-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Iain Arnell <iarnell@gmail.com> 1.011-3
- update filtering for rpm 4.9

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.011-2
- Perl mass rebuild

* Wed Apr 27 2011 Petr Pisar <ppisar@redhat.com> - 1.011-1
- 1.011 bump
- Move to ExtUtils::MakeMaker

* Tue Jan 25 2011 Petr Pisar <ppisar@redhat.com> 1.009-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
- Install into perl core directory
- Hack %%check for rpmbuild bug #672538
