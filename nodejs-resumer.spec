# spec file for package nodejs-nodejs-resumer
%{?scl:%scl_package nodejs-nodejs-resumer}
%{!?scl:%global pkg_name %{name}}

%global npm_name resumer
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-resumer
Version:	0.0.0
Release:	1%{?dist}
Summary:	A through stream that starts paused and resumes on the next tick
Url:		https://github.com/substack/resumer
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel
#BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	npm(concat-stream)
BuildRequires:	npm(tap)
BuildRequires:	npm(tape)
%endif

%description
A through stream that starts paused and resumes on the next tick

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
tap test/*.js
%endif

%files
%{nodejs_sitelib}/resumer

%doc readme.markdown LICENSE

%changelog
* Wed Jul 29 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.0.0-1
- Initial build
