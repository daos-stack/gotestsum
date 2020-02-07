%global debug_package %{nil}

Name:           gotestsum
Version:        0.4.0
Release:        1%{?dist}
Summary:        `go test` runner with output optimized for humans, JUnit XML for CI integration, and a summary of the test results

Group:          Development/Tools
License:        ASL 2.0
URL:            https://github.com/gotestyourself/gotestsum
Source0:        https://github.com/gotestyourself/%{name}/archive/v%{version}.tar.gz

BuildRequires:  go >= 1.11

%description
gotestsum runs tests, prints friendly test output and a summary of the test run.

%prep
%setup -q -n %{name}-%{version}%{?ver_add}

%build
go build -v

%install
install -d -m 755 %{buildroot}%{_bindir}
install -p -m 755 %{name} %{buildroot}%{_bindir}/

%files
%doc LICENSE NOTICE README.md
%{_bindir}/%{name}

%changelog
* Fri Feb 07 2020 Michael MacDonald <mjmac.macdonald@intel.com> - 0.4.0-1
- Initial package
