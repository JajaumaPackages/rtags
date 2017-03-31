# git describe --tags
%global commit 843dd06
%global vermagic 2.9
%global snapshot .git20170331.%{commit}

Name:           rtags
Version:        %{vermagic}
Release:        2%{?snapshot}%{?dist}
Summary:        A c/c++ client/server indexer for c/c++/objc[++]

License:        GPLv3+
URL:            https://github.com/Andersbakken/rtags
# git clone --recursive https://github.com/Andersbakken/rtags.git
# tar cfz rtags.tar.gz  rtags/
Source0:        rtags.tar.gz

BuildRequires:  cmake >= 2.8.6
BuildRequires:  llvm-devel >= 3.3
BuildRequires:  clang-devel >= 3.3
BuildRequires:  zlib-devel
BuildRequires:  openssl-devel
BuildRequires:  emacs
Requires:       emacs-filesystem

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
%{cmake} ..
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
%{_emacs_sitelispdir}/rtags/
%{_mandir}/man7/rc.7*
%{_mandir}/man7/rdm.7*


%changelog
* Fri Mar 31 2017 Jajauma's Packages <jajauma@yandex.ru> - 2.9-2.git20170331.843dd06
- Update to latest git snapshot

* Wed Mar 29 2017 Jajauma's Packages <jajauma@yandex.ru> - 2.9-1.git20170329.502b413
- Initial release
