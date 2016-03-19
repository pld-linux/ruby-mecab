Summary:	MeCab module for Ruby
Summary(pl.UTF-8):	Moduł MeCab dla języka Ruby
Name:		ruby-mecab
Version:	0.996
Release:	4
License:	GPL v2 or LGPL v2.1 or BSD
Group:		Development/Languages
# Source0Download: http://code.google.com/p/mecab/downloads/list
Source0:	http://mecab.googlecode.com/files/mecab-ruby-%{version}.tar.gz
# Source0-md5:	d72937048a8aeb3ae8da69139a959210
URL:		http://code.google.com/p/mecab/
BuildRequires:	libstdc++-devel
BuildRequires:	mecab-devel >= 0.996
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby-devel >= 1:1.8.6
Requires:	mecab >= 0.996
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MeCab module for Ruby.

%description -l pl.UTF-8
Moduł MeCab dla języka Ruby.

%prep
%setup -q -n mecab-ruby-%{version}

%build
%{__ruby} extconf.rb \
	--vendor

%{__make} \
	V=1 \
	CXX="%{__cc}" \
	CXXFLAGS="%{rpmcxxflags} -fPIC" \
	ldflags="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BSD COPYING README bindings.html
%attr(755,root,root) %{ruby_vendorarchdir}/MeCab.so
