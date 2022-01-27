Name:           armadillo
Version:        10.7.4
Release:        1
Summary:        Fast C++ matrix library with syntax similar to MATLAB and Octave
License:        ASL 2.0
URL:            http://arma.sourceforge.net/
Source:         http://sourceforge.net/projects/arma/files/%{name}-%{version}.tar.xz

BuildRequires:  cmake lapack-devel arpack-devel hdf5-devel openblas-devel SuperLU-devel gcc-g++


%description
Armadillo is a C ++ linear algebra library and is an important choice.

%package devel
Summary:        Development headers and documentation for the Armadillo C++ library
Requires:       %{name} = %{version}-%{release}
Requires:       lapack-devel arpack-devel libstdc++-devel hdf5-devel openblas-devel SuperLU-devel

%description devel
This package contains header files.

%package        help
Summary:        some doc for armadillo

%description    help
This help package contain some docs.

%prep
%autosetup -n %{name}-%{version} -p1

sed -i 's/\r//' README.md

%build
%{cmake}
%make_build VERBOSE=1

%install
%make_install

rm -f examples/{Makefile.cmake,example1_win64.sln,example1_win64.vcxproj,example1_win64.README.txt}
rm -rf examples/lib_win64

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_libdir}/libarmadillo.so.10*
%license LICENSE.txt NOTICE.txt

%files devel
%{_libdir}/libarmadillo.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/armadillo
%{_includedir}/armadillo_bits/
%{_datadir}/Armadillo/

%files help
%doc README.md index.html docs.html mex_interface
%doc examples armadillo_icon.png
%doc armadillo_nicta_2010.pdf rcpp_armadillo_csda_2014.pdf
%doc armadillo_joss_2016.pdf 

%changelog
* Fri Jan 21 2022 SimpleUpdate Robot <tc@openeuler.org> - 10.7.4-1
- Upgrade to version 10.7.4

* Mon May 31 2021 baizhonggui <baizhonggui@huawei.com> - 9.600.6-5
- Add gcc-g++ in BuildRequires

* Fri 26 Mar 2021 sunguoshuai <sunguoshuai@huawei.com> - 9.600.6-4
- Delete depends on atlas

* Thu Mar 5 2020 wangye <wangye54@huawei.com> - 9.600.6-3
- Update 

* Thu Mar 5 2020 wangye <wangye54@huawei.com> - 9.600.6-2
- Package init
