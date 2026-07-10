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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-durham
%dir %{_datadir}/texmf-dist/tex/latex/beamertheme-durham
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-durham/CHANGELOG.md
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-durham/LICENSE.txt
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-durham/README.md
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-durham/accessibility.png
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-durham/durham-demo.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-durham/durham-demo.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-durham/durham-manual.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-durham/durham-manual.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-durham/plain.png
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-durham/plain_accessibility.png
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-durham/plain_accessibility_invert.png
%{_datadir}/texmf-dist/tex/latex/beamertheme-durham/beamerthemedurham.sty
