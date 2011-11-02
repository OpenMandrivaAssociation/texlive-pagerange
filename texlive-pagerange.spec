Name:		texlive-pagerange
Version:	0.5
Release:	1
Summary:	Flexible and configurable page range typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pagerange
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagerange.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagerange.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package defines a command \pagerange that typesets ranges
of page numbers, expanding them (e.g., adding first or large
page numbers) and standardising them.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
