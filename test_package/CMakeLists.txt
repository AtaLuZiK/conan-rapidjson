project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

enable_testing()

add_custom_target(tests ALL)
link_libraries(${CONAN_LIBS})
add_subdirectory(perftest)
add_subdirectory(unittest)
