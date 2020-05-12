%global srcname ansible_role_tripleo_modify_image
%global rolename ansible-role-tripleo-modify-image

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{rolename}
Version:        XXX
Release:        XXX
Summary:        Ansible role to allow modification to container images built for the TripleO project.

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://git.openstack.org/cgit/openstack/ansible-role-tripleo-modify-image
Source0:        https://tarballs.openstack.org/%{rolename}/%{rolename}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires:       python3dist(ansible)


Requires: buildah

%description

Ansible role to allow modification to container images built for the TripleO project.

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%{py3_build}


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{py3_install}


%files
%doc README*
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/roles/


%changelog

