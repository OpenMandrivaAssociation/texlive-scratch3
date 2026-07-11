%global tl_name scratch3
%global tl_revision 61921

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.19
Release:	%{tl_revision}.1
Summary:	Draw programs like scratch
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/scratch3
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scratch3.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scratch3.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package permits to draw program charts in the style of the scatch
project (scratch.mit.edu). It depends on the other LaTeX packages TikZ
and simplekv.

