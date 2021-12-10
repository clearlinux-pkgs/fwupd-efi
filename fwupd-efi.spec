#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fwupd-efi
Version  : 1.1
Release  : 1
URL      : https://github.com/fwupd/fwupd-efi/archive/refs/tags/1.1.tar.gz
Source0  : https://github.com/fwupd/fwupd-efi/archive/refs/tags/1.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: fwupd-efi-libexec = %{version}-%{release}
Requires: fwupd-efi-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : gnu-efi-dev
BuildRequires : gnu-efi-staticdev

%description
# EFI executable for fwupd
This repository contains the source used for the fwupd project to generate a UEFI binary for installing updates using the `UpdateCapsule` runtime service.

%package dev
Summary: dev components for the fwupd-efi package.
Group: Development
Provides: fwupd-efi-devel = %{version}-%{release}
Requires: fwupd-efi = %{version}-%{release}

%description dev
dev components for the fwupd-efi package.


%package libexec
Summary: libexec components for the fwupd-efi package.
Group: Default
Requires: fwupd-efi-license = %{version}-%{release}

%description libexec
libexec components for the fwupd-efi package.


%package license
Summary: license components for the fwupd-efi package.
Group: Default

%description license
license components for the fwupd-efi package.


%prep
%setup -q -n fwupd-efi-1.1
cd %{_builddir}/fwupd-efi-1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639123651
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/fwupd-efi
cp %{_builddir}/fwupd-efi-1.1/COPYING %{buildroot}/usr/share/package-licenses/fwupd-efi/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/fwupd-efi-1.1/contrib/debian/signing-template/copyright %{buildroot}/usr/share/package-licenses/fwupd-efi/c1a12b921301c21ba9b3dc26e7db1d859bb8259d
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/fwupd-efi.pc

%files libexec
%defattr(-,root,root,-)
/usr/libexec/fwupd/efi/fwupdx64.efi

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fwupd-efi/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/fwupd-efi/c1a12b921301c21ba9b3dc26e7db1d859bb8259d
