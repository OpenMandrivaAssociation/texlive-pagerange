# revision 16915
# category Package
# catalog-ctan /macros/latex/contrib/pagerange
# catalog-date 2010-02-04 09:04:58 +0100
# catalog-license lppl
# catalog-version 0.5
Name:		texlive-pagerange
Version:	0.5
Release:	9
Summary:	Flexible and configurable page range typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pagerange
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagerange.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pagerange.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.5-2
+ Revision: 754626
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.5-1
+ Revision: 719182
- texlive-pagerange
- texlive-pagerange
- texlive-pagerange
- texlive-pagerange

