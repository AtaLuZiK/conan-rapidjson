from os import path

from conans import CMake, ConanFile, tools


class RapidjsonConan(ConanFile):
    name = "rapidjson"
    version = "1.1.0"
    license = "https://raw.githubusercontent.com/Tencent/rapidjson/v1.1.0/license.txt"
    url = "https://github.com/AtaLuZiK/conan-rapidjson"
    repo_url = "https://github.com/Tencent/rapidjson.git"
    description = "<Description of Rapidjson here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "cxx11": [True, False],
        "asan": [True, False],
        "ubsan": [True, False],
        "stdstring": [True, False],
    }
    default_options = "\n".join([
        "cxx11=True",
        "asan=False",
        "ubsan=False",
        "stdstring=False",
    ])
    generators = "cmake"

    def source(self):
        self.run("git clone -b v%s --depth 1 %s" % (self.version, self.repo_url))
        tools.replace_in_file("%s/CMakeLists.txt" % self.name, "PROJECT(RapidJSON CXX)", """PROJECT(RapidJSON CXX)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()""")


    def build(self):
        cmake = CMake(self)

        # Configure
        command_line = [
            cmake.command_line,
            "-DRAPIDJSON_BUILD_DOC=OFF",
            "-DRAPIDJSON_BUILD_EXAMPLES=OFF",
            "-DRAPIDJSON_BUILD_TESTS=OFF",
            "-DRAPIDJSON_BUILD_THIRDPARTY_GTEST=OFF",
            self.cmake_build_option("cxx11"),
            self.cmake_build_option("asan"),
            self.cmake_build_option("ubsan"),
            self.cmake_has_option("stdstring"),
        ]
        self.run("cmake %s %s" % (path.join(self.source_folder, self.name), " ".join(command_line)))

        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="rapidjson/include")

    def cmake_option_bool(self, name, cmake_name):
        return "-D%s=%s" % (cmake_name, ("ON" if getattr(self.options, name) else "OFF"))

    def cmake_build_option(self, name):
        return self.cmake_option_bool(name, "RAPIDJSON_BUILD_%s" % name.upper())

    def cmake_has_option(self, name):
        return self.cmake_option_bool(name, "RAPIDJSON_HAS_%s" % name.upper())
