%global tl_name beamertheme-durham
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.0
Release:	%{tl_revision}.1
Summary:	A content-first Beamer theme for teaching, research, and long-form academic p...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamertheme-durham
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-durham.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-durham.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the Durham Beamer Theme, a content-first
presentation theme for LaTeX Beamer designed for teaching, research, and
long-form academic presentations. The theme emphasizes structural
clarity, pacing awareness, and layout stability under dense textual and
mathematical content. It is implemented entirely from first principles
and not derived from any existing Beamer theme. Conceptual inspiration
from established themes such as Metropolis is acknowledged; no external
code is reused. The color palette is inspired by the visual identity of
Durham University. This package is an independent academic contribution
and not an official or endorsed Durham University template. The package
includes a modular theme implementation, a demo document with compiled
PDF, and a user manual.

