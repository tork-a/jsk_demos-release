Name:           ros-indigo-jsk-maps
Version:        0.0.3
Release:        1%{?dist}
Summary:        ROS jsk_maps package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_maps
Source0:        %{name}-%{version}.tar.gz

Requires:       ImageMagick
Requires:       ros-indigo-euslisp
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-jsk-rviz-plugins
Requires:       ros-indigo-jskeus
Requires:       ros-indigo-multi-map-server
BuildRequires:  ImageMagick
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-euslisp
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-jsk-rviz-plugins
BuildRequires:  ros-indigo-jskeus
BuildRequires:  ros-indigo-multi-map-server

%description
jsk_maps

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Feb 11 2016 Manabu Saito, Haseru Chen and Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.0.3-1
- Autogenerated by Bloom

