# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate blake2

Name:           rust-%{crate}
Version:        0.8.1
Release:        2%{?dist}
Summary:        BLAKE2 hash functions

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/blake2
Source:         %{crates_source}
# Initial patched metadata
# * Update hex-literal to 0.2, https://github.com/RustCrypto/hashes/pull/85
Patch0:         blake2-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
BLAKE2 hash functions.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+simd-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+simd-devel %{_description}

This package contains library source intended for building other packages
which use "simd" feature of "%{crate}" crate.

%files       -n %{name}+simd-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+simd_asm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+simd_asm-devel %{_description}

This package contains library source intended for building other packages
which use "simd_asm" feature of "%{crate}" crate.

%files       -n %{name}+simd_asm-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+simd_opt-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+simd_opt-devel %{_description}

This package contains library source intended for building other packages
which use "simd_opt" feature of "%{crate}" crate.

%files       -n %{name}+simd_opt-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 05:41:25 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 09:59:41 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-2
- Run tests in infrastructure

* Sat Mar 16 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.0-1
- Initial package
