%define libname %mklibname %{name} %{version}
%define devname %mklibname %{name} -d

Summary:	CommonMark parsing and rendering
Name:		cmark
Version:	0.28.3
Release:	1
License:	BSD and MIT
Group:		Development/Tools
Url:		https://github.com/jgm/cmark
Source0:	https://github.com/jgm/cmark/archive/%{version}.tar.gz?/%{name}-%{version}.tar.gz
BuildRequires:	cmake

%description
`cmark` is the C reference implementation of CommonMark,
a rationalized version of Markdown syntax with a spec.

It provides a shared library (`libcmark`) with functions for parsing
CommonMark documents to an abstract syntax tree (AST), manipulating
the AST, and rendering the document to HTML, groff man, LaTeX,
CommonMark, or an XML representation of the AST.  It also provides a
command-line program (`cmark`) for parsing and rendering CommonMark
documents.

%files
%doc COPYING README.md
%{_bindir}/cmark
%{_mandir}/man1/cmark.1*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	CommonMark parsing and rendering library
Group:		System/Libraries

%description -n %{libname}
This package provides the cmark shared library.

%files -n %{libname}
%{_libdir}/libcmark.so.%{version}

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for cmark
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package provides the development files for cmark.

%files -n %{devname}
%{_includedir}/cmark.h
%{_includedir}/cmark_export.h
%{_includedir}/cmark_version.h
%{_libdir}/libcmark.so
%{_libdir}/pkgconfig/libcmark.pc
%{_mandir}/man3/cmark.3*
%{_libdir}/cmake/cmark*.cmake

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake \
	-DCMARK_TESTS=OFF
%make

%install
%makeinstall_std -C build

rm %{buildroot}%{_libdir}/libcmark.a

