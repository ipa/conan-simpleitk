project(SimpleITKTest CXX)
cmake_minimum_required(VERSION 3.1.2)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(test_sitk test.cpp)
conan_target_link_libraries(test_sitk)

target_link_libraries(test_sitk CONAN_PKG::SimpleITK)

# CTest is a testing tool that can be used to test your project.
enable_testing()
add_test(NAME test_sitk WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin COMMAND test_sitk)
