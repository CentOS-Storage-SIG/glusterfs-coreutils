# this commit points to https://github.com/gluster/glusterfs-coreutils/pull/4
%global commit0 0c86f7f8459f4f743d7fe7cacdfb902768ee5f87
# % global gittag0 GIT-TAG
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary:          Core Utilities for the Gluster Distributed File System
Name:             glusterfs-coreutils
Version:          0.0.1
Release:          0.1.git%{shortcommit0}%{?dist}
Vendor:           Gluster Community
License:          GPLv3
Group:            System Environment/Base
BuildRequires:    glusterfs-api-devel >= 3.6.0
BuildRequires:    help2man >= 1.36
URL:              http://www.gluster.org
#
# The source tarball on GitHub does not contain the ./configure and other
# generated bits that should be part of a release. Download the original
# tarball, unpack and run "./autogen.sh && ./configure && make dist" to
# generate the tarball for this RPM.
#Source0:          https://github.com/gluster/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source0:          %{name}-%{shortcommit0}-prep.tar.gz

%description
gluster-coreutils provides a set of basic utilities such as cat, mkdir, ls, and
tail that are implemented specifically using the GlusterFS API.

%prep
%setup -qn %{name}-%{shortcommit0}

%build
%configure
make

%install
make DESTDIR=${RPM_BUILD_ROOT} install

for i in gfcat gfcp gfmkdir gfls gfrm gfstat gftail; do
        ln -fs %{_bindir}/gfcli ${RPM_BUILD_ROOT}%{_bindir}/$i
done

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
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
* Fri Aug 21 2015 Niels de Vos <ndevos@redhat.com> - 0.0.1-0.1.git0c86f7f
- initial packaging based on upstream .spec
- remove build dependency on libtirpc (pull request #4)

