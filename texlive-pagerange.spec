Name:		texlive-pagerange
Version:	16915
Release:	1
Summary:	Flexible and configurable page range typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pagerange
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagerange.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagerange.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a command \pagerange that typesets ranges
of page numbers, expanding them (e.g., adding first or large
page numbers) and standardising them.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pagerange/pagerange-guide.cfg
%{_texmfdistdir}/tex/latex/pagerange/pagerange.sty
%doc %{_texmfdistdir}/doc/latex/pagerange/README
%doc %{_texmfdistdir}/doc/latex/pagerange/pagerange-guide.pdf
%doc %{_texmfdistdir}/doc/latex/pagerange/pagerange-guide.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
