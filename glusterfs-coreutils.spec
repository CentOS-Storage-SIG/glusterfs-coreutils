%global commit0 259f269f7a4345eabe419c29ce51a2d2a8346e19
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary:          Core Utilities for the Gluster Distributed File System
Name:             glusterfs-coreutils
Version:          0.0.1
Release:          0.1.git%{shortcommit0}%{?dist}
License:          GPLv3
Group:            System Environment/Base
URL:              https://github.com/gluster/glusterfs-coreutils
# The source for this package was created from upstream source using the
# following command:
#       make dist
Source0:          %{name}-%{shortcommit0}.tar.gz

Provides:         bundled(gnulib)

Requires:         glusterfs-api >= 3.6.0

BuildRequires:    glusterfs-api-devel >= 3.6.0
BuildRequires:    help2man >= 1.36
BuildRequires:    readline-devel

%description
gluster-coreutils provides a set of basic utilities such as cat, mkdir, ls,
stat, rm and tail that are implemented specifically using the GlusterFS API.

%prep
%setup -q -n %{name}-%{shortcommit0}

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%{_bindir}/gfcat
%{_bindir}/gfcli
%{_bindir}/gfcp
%{_bindir}/gfls
%{_bindir}/gfmkdir
%{_bindir}/gfput
%{_bindir}/gfrm
%{_bindir}/gfstat
%{_bindir}/gftail
%{_mandir}/man1/gfcat.1.gz
%{_mandir}/man1/gfcli.1.gz
%{_mandir}/man1/gfcp.1.gz
%{_mandir}/man1/gfls.1.gz
%{_mandir}/man1/gfmkdir.1.gz
%{_mandir}/man1/gfput.1.gz
%{_mandir}/man1/gfrm.1.gz
%{_mandir}/man1/gfstat.1.gz
%{_mandir}/man1/gftail.1.gz

%changelog
* Fri Jun 03 2016 Anoop C S <anoopcs@redhat.com> - 0.0.1-0.1.git259f269
- Fixed unused variable build error

* Thu May 05 2016 Anoop C S <anoopcs@redhat.com> - 0.0.1-0.4.git60d57d8
- Fixed creation of links within upstream

* Fri Apr 29 2016 Anoop C S <anoopcs@redhat.com> - 0.0.1-0.3.gitf9a4a2e
- Initial package based on upstream spec file

