# TODO: php, ruby
#
# Conditional build:
%bcond_without	static_libs	# static libraries
%bcond_without	cxx		# C++ binding
%bcond_without	java		# Java binding
%bcond_without	perl		# Perl binding
%bcond_without	python		# Python binding
%bcond_with	ruby		# Ruby binding (not finished in sources)
%bcond_without	tcl		# Tcl binding
%bcond_with	system_libjpeg	# system libjpeg library (included libtiff relies on libjpeg = 6b)
%bcond_without	system_libpng	# system libpng library
%bcond_with	system_libtiff	# system libtiff library (PDFLib uses modified version)
%bcond_without	system_zlib	# system ZLib library
#

%{?with_java:%{?use_default_jdk}}

Summary:	PDFlib - A library for generating PDF on the fly
Summary(pl.UTF-8):	PDFlib - biblioteka do tworzenia plików PDF w locie
Name:		pdflib-lite
Version:	7.0.5p3
Release:	5
License:	free for personal use
Group:		Libraries
# originally http://www.pdflib.com/download/pdflib-family/pdflib-lite-7/ but no longer available;
# use a copy from other distro repo
Source0:	http://ponce.cc/slackware/sources/repo/PDFlib-Lite-%{version}.tar.gz
# Source0-md5:	371d332d610a8b21a542bb7a2bdaf954
Patch0:		%{name}-format.patch
Patch1:		%{name}-tcl.patch
Patch2:		%{name}-modules.patch
Patch3:		%{name}-perl.patch
Patch4:		%{name}-python.patch
Patch5:		%{name}-libtool.patch
Patch6:		%{name}-system-libs.patch
Patch7:		%{name}-shared.patch
Patch8:		java-compat.patch
Patch9:		java-paths.patch
URL:		https://www.pdflib.com/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_java:%buildrequires_jdk}
%{?with_system_libjpeg:BuildRequires:	libjpeg-devel >= 6b}
%{?with_system_libpng:BuildRequires:	libpng-devel >= 2:1.2.36}
%{?with_cxx:BuildRequires:	libstdc++-devel}
%{?with_system_libtiff:BuildRequires:	libtiff-devel >= 3.7.4}
BuildRequires:	libtool
%{?with_perl:BuildRequires:	perl-devel >= 5}
%{?with_python:BuildRequires:	python-devel >= 2}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 2.021
%{?with_tcl:BuildRequires:	tcl-devel >= 8.2}
%{?with_system_zlib:BuildRequires:	zlib-devel >= 1.2.3}
%{?with_system_libjpeg:Requires:	libjpeg >= 6b}
%{?with_system_libpng:Requires:	libpng >= 2:1.2.36}
%{?with_system_libtiff:Requires:	libtiff >= 3.7.4}
%{?with_system_zlib:Requires:	zlib >= 1.2.3}
Obsoletes:	pdflib < 5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		tcl_ver		%(echo `echo "puts [info tclversion]" | tclsh`)
%define		tcl_libdir	%{_libdir}/tcl%{tcl_ver}

%description
PDFlib is a library for generating PDF files. It offers an API with
support for text, vector graphics, raster image, and hypertext. Call
PDFlib routines from within your client program and voila: dynamic PDF
files!

PDFlib Lite is an open-source edition for basic PDF generation, free
for personal use. PDFlib Lite does not support all languages, and is
not available on EBCDIC platforms. PDFlib Lite supports only a subset
of PDFlib features.

%description -l pl.UTF-8
PDFlib to biblioteka do generowania plików PDF. Oferuje API z obsługą
tekstu, grafiki wektorowej, obrazów rastrowych i hipertekstu. Funkcje
biblioteki PDFlib można wywoływać z programów klienckich, otrzymując
dynamiczne pliki PDF.

PDFlib Lite to wydanie biblioteki z otwartymi źródłami, pozwalające na
generowanie podstawowych plików PDF, darmowe do użytku osobistego. Nie
obsługuje wszystkich języków, nie jest dostępne na platformach EBCDIC.
Obsługuje tylko podzbiór możliwości pełnej wersji biblioteki PDFlib.

%package devel
Summary:	Header file for PDFlib Lite library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki PDFlib Lite
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_system_libjpeg:BuildRequires:	libjpeg-devel >= 6b}
%{?with_system_libpng:BuildRequires:	libpng-devel >= 2:1.2.36}
%{?with_system_libtiff:BuildRequires:	libtiff-devel >= 3.7.4}
%{?with_system_zlib:BuildRequires:	zlib-devel >= 1.2.3}
Obsoletes:	pdflib-devel < 5

%description devel
Header file for PDFlib Lite library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki PDFlib Lite.

%package static
Summary:	Static PDFlib Lite library
Summary(pl.UTF-8):	Statyczna biblioteka PDFlib Lite
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	pdflib-static < 5

%description static
Static PDFlib Lite library.

%description static -l pl.UTF-8
Statyczna biblioteka PDFlib Lite.

%package c++
Summary:	C++ binding for PDFlib Lite library
Summary(pl.UTF-8):	Wiązania C++ do biblioteki PDFlib Lite
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
C++ binding for PDFlib Lite library.

%description c++ -l pl.UTF-8
Wiązania C++ do biblioteki PDFlib Lite.

%package c++-devel
Summary:	Header file for C++ PDFlib Lite binding
Summary(pl.UTF-8):	Plik nagłówkowy wiązań C++ do biblioteki PDFlib Lite
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
Header file for C++ PDFlib Lite binding.

%description c++-devel -l pl.UTF-8
Plik nagłówkowy wiązań C++ do biblioteki PDFlib Lite.

%package c++-static
Summary:	Static C++ PDFlib Lite binding library
Summary(pl.UTF-8):	Statyczna biblioteka wiązań C++ do biblioteki PDFlib Lite
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
Static C++ PDFlib Lite binding library.

%description c++-static -l pl.UTF-8
Statyczna biblioteka wiązań C++ do biblioteki PDFlib Lite.

%package -n java-pdflib-lite
Summary:	Java bindings for PDFlib Lite library
Summary(pl.UTF-8):	Wiązania Javy do biblioteki PDFlib Lite
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Obsoletes:	pdflib-java < 5

%description -n java-pdflib-lite
Java bindings for PDFlib Lite library.

%description -n java-pdflib-lite -l pl.UTF-8
Wiązania Javy do biblioteki PDFlib Lite.

%package -n java-pdflib-lite-javadoc
Summary:	Documentation for Java PDFlib Lite binding
Summary(pl.UTF-8):	Dokumentacja wiązań Javy do biblioteki PDFlib Lite
Group:		Documentation
BuildArch:	noarch

%description -n java-pdflib-lite-javadoc
Documentation for Java PDFlib Lite binding.

%description -n java-pdflib-lite-javadoc -l pl.UTF-8
Dokumentacja wiązań Javy do biblioteki PDFlib Lite.

%package -n perl-pdflib-lite
Summary:	Perl bindings for PDFlib Lite library
Summary(pl.UTF-8):	Wiązania Perla do biblioteki PDFlib Lite
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Obsoletes:	pdflib-perl < 5
Obsoletes:	pdflib-perl5 < 5

%description -n perl-pdflib-lite
Perl bindings for PDFlib Lite library.

%description -n perl-pdflib-lite -l pl.UTF-8
Wiązania Perla do biblioteki PDFlib Lite.

%package -n python-pdflib-lite
Summary:	Python 2 bindings for PDFlib Lite library
Summary(pl.UTF-8):	Wiązania Pythona 2 do biblioteki PDFlib Lite
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Obsoletes:	pdflib-python < 5
Obsoletes:	pdflib-python1.5 < 5

%description -n python-pdflib-lite
Python 2 bindings for PDFlib Lite library.

%description -n python-pdflib-lite -l pl.UTF-8
Wiązania Pythona 2 do biblioteki PDFlib Lite.

%package -n tcl-pdflib-lite
Summary:	Tcl bindings for PDFlib Lite library
Summary(pl.UTF-8):	Wiązania Tcl-a do biblioteki PDFlib Lite
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}
Obsoletes:	pdflib-tcl < 5
Obsoletes:	pdflib-tcl8.0 < 5

%description -n tcl-pdflib-lite
Tcl bindings for PDFlib Lite library.

%description -n tcl-pdflib-lite -l pl.UTF-8
Wiązania Tcl-a do biblioteki PDFlib Lite.

%prep
%setup -q -n PDFlib-Lite-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%{?with_system_zlib:%{__rm} -r libs/flate}
%{?with_system_zlib:%{__sed} -i -e '/\/flate\// d' libs/pdflib/Make_objs2.inc}
%{?with_system_libjpeg:%{__rm} -r libs/jpeg}
%{?with_system_libjpeg:%{__sed} -i -e '/\/jpeg\// d' libs/pdflib/Make_objs2.inc}
%{?with_system_libpng:%{__rm} -r libs/png}
%{?with_system_libpng:%{__sed} -i -e '/\/png\// d' libs/pdflib/Make_objs2.inc}
%{?with_system_libtiff:%{__rm} -r libs/tiff}
%{?with_system_libtiff:%{__sed} -i -e '/\/tiff\// d' libs/pdflib/Make_objs2.inc}

: >config/aclocal.m4

%build
%{__libtoolize}
%{__aclocal} --output config/aclocal.m4
%{__autoconf}
%configure \
	PYTHONBIN="%{__python}" \
	%{!?with_cxx:--disable-cxx} \
	%{!?with_static_libs:--disable-static} \
	--with-java=%{?with_java:%{java_home}}%{!?with_java:no} \
%if %{with perl}
	--with-perl=%{__perl} \
	--with-perlincl=%{perl_archlib}/CORE \
%else
	--without-perl \
%endif
%if %{with python}
	--with-py=%{py_sitedir} \
	--with-pyincl=%{py_incdir} \
%else
	--without-py \
%endif
%if %{with ruby}
	--with-ruby=%{__ruby} \
	--with-rubyincl=%{ruby_rubyhdrdir} \
%else
	--without-ruby \
%endif
%if %{with tcl}
	--with-tcl=%{_bindir}/tclsh \
	--with-tclpkg=%{_libdir}/tcl%{tcl_ver} \
%else
	--without-tcl
%endif

%{__make} \
	JAVA_EXE="%{java_home}/bin/java" \
	JAVAC_EXE="%{java_home}/bin/javac" \
	JAR="%{java_home}/bin/jar"

%if %{with cxx}
cd bind/pdflib/cpp
../../../libtool --mode=link %{__cxx} -o libpdf_cpp.la pdflib.lo ../../../libs/pdflib/libpdf.la -rpath %{_libdir}
cd ../../..
%endif

%if %{with java}
%{__make} JAVADOC="%{java_home}/bin/javadoc" -C bind/pdflib/java javadoc
%endif

%if %{with perl}
%{__make} -C bind/pdflib/perl
%endif

%if %{with python}
%{__make} -C bind/pdflib/python
%endif

%if %{with ruby}
%{__make} -C bind/pdflib/ruby
%endif

%if %{with tcl}
%{__make} -C bind/pdflib/tcl
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with cxx}
cd bind/pdflib/cpp
../../../libtool --mode=install install libpdf_cpp.la $RPM_BUILD_ROOT%{_libdir}
cp -p pdflib.hpp $RPM_BUILD_ROOT%{_includedir}
cd ../../..
%endif

%if %{with java}
install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}}
cp -p bind/pdflib/java/pdflib.jar $RPM_BUILD_ROOT%{_javadir}
cp -pr bind/pdflib/java/javadoc $RPM_BUILD_ROOT%{_javadocdir}/pdflib
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libpdf_java.la
%endif

%if %{with perl}
install -d $RPM_BUILD_ROOT%{perl_vendorarch}
%{__make} -C bind/pdflib/perl install \
	DESTDIR=$RPM_BUILD_ROOT
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/pdflib_pl.la
%endif

%if %{with python}
install -d $RPM_BUILD_ROOT%{py_sitedir}
%{__make} -C bind/pdflib/python install \
	DESTDIR=$RPM_BUILD_ROOT
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/pdflib_py.la
%endif

%if %{with ruby}
%{__make} -C bind/pdflib/ruby install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with tcl}
%{__make} -C bind/pdflib/tcl install \
	DESTDIR=$RPM_BUILD_ROOT
%{__rm} $RPM_BUILD_ROOT%{tcl_libdir}/pdflib/pdflib_tcl.la
%endif

# ensure soname deps are generated
find $RPM_BUILD_ROOT%{_libdir} -name '*.so*' | xargs chmod 755

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%post	-n java-pdflib-lite -p /sbin/ldconfig
%postun	-n java-pdflib-lite -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme.txt doc/PDFlib-terms-and-conditions.pdf doc/pdflib/{PDFlib-Lite-license.pdf,changes.txt}
%attr(755,root,root) %{_bindir}/pdfimage
%attr(755,root,root) %{_bindir}/text2pdf
%attr(755,root,root) %{_libdir}/libpdf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpdf.so.6

%files devel
%defattr(644,root,root,755)
%doc doc/pdflib/{PDFlib-API-reference.pdf,PDFlib-tutorial.pdf,compatibility.txt}
%attr(755,root,root) %{_bindir}/pdflib-config
%attr(755,root,root) %{_libdir}/libpdf.so
%{_libdir}/libpdf.la
%{_includedir}/pdflib.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libpdf.a
%endif

%if %{with cxx}
%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpdf_cpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpdf_cpp.so.0

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpdf_cpp.so
%{_libdir}/libpdf_cpp.la
%{_includedir}/pdflib.hpp

%if %{with static_libs}
%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libpdf_cpp.a
%endif
%endif

%if %{with java}
%files -n java-pdflib-lite
%defattr(644,root,root,755)
%doc bind/pdflib/java/readme.txt
%attr(755,root,root) %{_libdir}/libpdf_java.so
%{_javadir}/pdflib.jar

%files -n java-pdflib-lite-javadoc
%defattr(644,root,root,755)
%{_javadocdir}/pdflib
%endif

%if %{with perl}
%files -n perl-pdflib-lite
%defattr(644,root,root,755)
%doc bind/pdflib/perl/readme.txt
%{perl_vendorarch}/pdflib_pl.pm
%attr(755,root,root) %{perl_vendorarch}/pdflib_pl.so
%endif

%if %{with perl}
%files -n python-pdflib-lite
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/pdflib_py.so
%endif

%if %{with tcl}
%files -n tcl-pdflib-lite
%defattr(644,root,root,755)
%doc bind/pdflib/tcl/readme.txt
%dir %{tcl_libdir}/pdflib
%attr(755,root,root) %{tcl_libdir}/pdflib/pdflib_tcl.so
%{tcl_libdir}/pdflib/pkgIndex.tcl
%endif
