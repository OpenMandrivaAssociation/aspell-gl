%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.5a-2

%define languageenglazy Galician
%define languagecode gl
%define lc_ctype gl_ES

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Epoch:		1
Version:	0.5a.2
Release:	14
Group:		System/Internationalization
Url:		http://aspell.net/
License:	GPLv2
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell6-%{languagecode}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= 0.60
Requires:	aspell >= 0.60
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
Provides:	spell-%{languagecode}
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn aspell6-gl-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
%makeinstall_std

mv -f README README.%{languagecode}
chmod 644 Copyright README.%{languagecode} doc/*

%files
%doc README.%{languagecode} Copyright 
%doc doc/*
%{_libdir}/aspell-*/*

