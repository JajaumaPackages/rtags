%global gitdate 20180328
%global gitversion 2.18
%global gitcommit a595d13

Name:           rtags
Version:        %{gitversion}
Release:        1.git%{gitdate}.%{gitcommit}%{?dist}
Summary:        A c/c++ client/server indexer for c/c++/objc[++]

License:        GPLv3+
URL:            https://github.com/Andersbakken/rtags
Source0:        rtags.tar.bz2

BuildRequires:  cmake >= 2.8.6
BuildRequires:  llvm-devel >= 3.3
BuildRequires:  clang-devel >= 3.3
BuildRequires:  zlib-devel
BuildRequires:  openssl-devel
BuildRequires:  bash-completion

%description
RTags is a client/server application that indexes C/C++ code and keeps a
persistent file-based database of references, declarations, definitions,
symbolnames etc. There’s also limited support for ObjC/ObjC++. It allows you to
find symbols by name (including nested class and namespace scope).

%prep
%setup -q -n rtags


%build
mkdir build
pushd build
# building with gcc 4.8.5 is not supported
export CC=/usr/bin/clang
export CXX=/usr/bin/clang++
# hide FORTIFY_SOURCE redefinition warning
export CFLAGS="$(echo %{optflags} | sed -e 's/-Wp,-D_FORTIFY_SOURCE=2//')"
export CXXFLAGS="$CFLAGS"
%{cmake} -DRTAGS_NO_ELISP_FILES=1 ..
make %{?_smp_mflags}
popd


%install
rm -rf %{buildroot}
pushd build
%make_install
popd build


%files
%license LICENSE.txt
%{_bindir}/rdm
%{_bindir}/rc
%{_bindir}/rp
%{_bindir}/gcc-rtags-wrapper.sh
%{_datadir}/bash-completion/
%{_mandir}/man7/rc.7*
%{_mandir}/man7/rdm.7*


%changelog
* Wed Mar 28 2018 Jajauma's Packages <jajauma@yandex.ru> - 2.18-1.git20180328.a595d13
- Update to latest git snapshot
- Disable elisp support

* Sat Mar 17 2018 Jajauma's Packages <jajauma@yandex.ru> - 2.18-1.git20180317.6f084a3
- Update to latest git snapshot

* Mon Nov 20 2017 Jajauma's Packages <jajauma@yandex.ru> - 2.15-1.git20171120.7de799d
- Update to latest git snapshot

* Thu Sep 14 2017 Jajauma's Packages <jajauma@yandex.ru> - 2.14-1.git20170914.2af4d6a3
- Update to latest git snapshot

* Tue Aug 22 2017 Jajauma's Packages <jajauma@yandex.ru> - 2.12-1.git20170822.8254e0b
- Update to latest git snapshot

* Fri Mar 31 2017 Jajauma's Packages <jajauma@yandex.ru> - 2.9-2.git20170331.843dd06
- Update to latest git snapshot

* Wed Mar 29 2017 Jajauma's Packages <jajauma@yandex.ru> - 2.9-1.git20170329.502b413
- Initial release
