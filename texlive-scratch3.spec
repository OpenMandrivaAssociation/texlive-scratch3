Name:		texlive-scratch3
Version:	61921
Release:	2
Summary:	Draw programs like "scratch"
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/scratch3
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scratch3.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scratch3.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package permits to draw program charts in the style of the
scatch project (scratch.mit.edu). It depends on the other LaTeX
packages TikZ and simplekv.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/scratch3
%doc %{_texmfdistdir}/doc/latex/scratch3

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
