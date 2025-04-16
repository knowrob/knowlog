cmake_minimum_required(VERSION 3.5.0)
set(PROJECT_VERSION 1.0.0)

project(knowlog
        VERSION ${PROJECT_VERSION}
        HOMEPAGE_URL "https://github.com/knowrob/knowlog")

find_package(catkin REQUIRED)
find_package(knowrob REQUIRED)

catkin_package(
	CATKIN_DEPENDS rospy
	DEPENDS knowrob)

catkin_install_python(PROGRAMS
	scripts/knowlog.py
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

