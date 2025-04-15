cmake_minimum_required(VERSION 3.5.0)
set(PROJECT_VERSION 1.0.0)

project(knowlog
        VERSION ${PROJECT_VERSION}
        HOMEPAGE_URL "https://github.com/knowrob/knowlog")

find_package(catkin REQUIRED)
find_package(knowrob REQUIRED)

catkin_package(
   #INCLUDE_DIRS include
   LIBRARIES ${PROJECT_NAME}
   CATKIN_DEPENDS rospy
   DEPENDS knowrob)

