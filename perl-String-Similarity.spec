#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-String-Similarity
Version  : 1.04
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/String-Similarity-1.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/String-Similarity-1.04.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libstring-similarity-perl/libstring-similarity-perl_1.04-2.debian.tar.xz
Summary  : ~
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-String-Similarity-license = %{version}-%{release}
Requires: perl-String-Similarity-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
String::Similarity - calculate the similarity of two strings
SYNOPSIS
use String::Similarity;

%package dev
Summary: dev components for the perl-String-Similarity package.
Group: Development
Provides: perl-String-Similarity-devel = %{version}-%{release}
Requires: perl-String-Similarity = %{version}-%{release}

%description dev
dev components for the perl-String-Similarity package.


%package license
Summary: license components for the perl-String-Similarity package.
Group: Default

%description license
license components for the perl-String-Similarity package.


%package perl
Summary: perl components for the perl-String-Similarity package.
Group: Default
Requires: perl-String-Similarity = %{version}-%{release}

%description perl
perl components for the perl-String-Similarity package.


%prep
%setup -q -n String-Similarity-1.04
cd %{_builddir}
tar xf %{_sourcedir}/libstring-similarity-perl_1.04-2.debian.tar.xz
cd %{_builddir}/String-Similarity-1.04
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/String-Similarity-1.04/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-String-Similarity
cp %{_builddir}/String-Similarity-1.04/COPYING %{buildroot}/usr/share/package-licenses/perl-String-Similarity/48d348ad54ae95b9aafcc5c9f1adcf555449a3b8
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-String-Similarity/8dd9ea654c60425670bacfcd78a6891f018a1a6b
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/String::Similarity.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-String-Similarity/48d348ad54ae95b9aafcc5c9f1adcf555449a3b8
/usr/share/package-licenses/perl-String-Similarity/8dd9ea654c60425670bacfcd78a6891f018a1a6b

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/String/Similarity.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/String/Similarity/Similarity.so
