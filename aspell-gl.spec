%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.5a-2

%define languageenglazy Galician
%define languagecode gl
%define lc_ctype gl_ES

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Epoch:         1
Version:       0.5a.2
Release:       %mkrel 6
Group:         System/Internationalization
Source:        ftp://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell6-%{languagecode}-%{src_ver}.tar.bz2
URL:           http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}

BuildRequires: aspell >= 0.60
BuildRequires: make
Requires:      aspell >= 0.60

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n aspell6-gl-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

mv -f README README.%{languagecode}
chmod 644 Copyright README.%{languagecode} doc/*

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.%{languagecode} Copyright 
%doc doc/*
%{_libdir}/aspell-*/*


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.5a.2-6mdv2011.0
+ Revision: 662823
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.5a.2-5mdv2011.0
+ Revision: 603212
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.5a.2-4mdv2010.1
+ Revision: 524199
- duh!
- fix build
- rebuilt for 2010.1
- rebuild

  + Funda Wang <fwang@mandriva.org>
    - add epoch
    - fix name and requires
    - revert renaming
    - rename

  + Christophe Fergeau <cfergeau@mandriva.com>
    - rebuild

  + Isabel Vallejo <isabel@mandriva.org>
    - update to 0.5a-2

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.50.0-7mdv2009.1
+ Revision: 350028
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.50.0-6mdv2009.0
+ Revision: 220381
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.50.0-5mdv2008.1
+ Revision: 182449
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.50.0-4mdv2008.1
+ Revision: 148775
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.50.0-3mdv2007.0
+ Revision: 123261
- Import aspell-gl

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.50.0-3mdv2007.1
- use the mkrel macro
- disable debug packages

* Fri Dec 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.50.0-2mdk
- rebuild for new aspell

* Tue Jul 20 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.50.0-1mdk
- first version for mandrake

