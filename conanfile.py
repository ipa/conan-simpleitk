from conans import ConanFile, CMake, tools

class NDICAPIConan(ConanFile):
    name = "SimpleITK"
    version = "1.2.0"
    description = "Simple ITK"
    url = "https://itk.org/SimpleITK.git"
    license = "Apache"
    exports = []
    source_subfolder = "source_subfolder"
    settings = "os", "compiler", "build_type", "arch"
    options = {}
    default_options = ""
    generators = "cmake"

    def source(self):
        self.run("git clone -b release https://itk.org/SimpleITK.git")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_INSTALL_PREFIX"] = "install"
        cmake.definitions["CMAKE_BUILD_EXAMPLE"] = "OFF"
        cmake.definitions["CMAKE_TESTING"] = "OFF"
        cmake.definitions["BUILD_TESTING"] = "OFF"
        cmake.definitions["WRAP_CSHARP"] = "OFF"
        cmake.definitions["WRAP_DEFAULT"] = "OFF"
        cmake.definitions["WRAP_JAVA"] = "OFF"
        cmake.definitions["WRAP_LUA"] = "OFF"
        cmake.definitions["WRAP_PYTHON"] = "OFF"
        cmake.definitions["WRAP_R"] = "OFF"
        cmake.definitions["WRAP_RUBY"] = "OFF"
        cmake.definitions["WRAP_TCL"] = "OFF"
        cmake.definitions["BUILD_SHARED_LIBS"] = "ON"
        cmake.configure(source_folder="SimpleITK/SuperBuild")
        cmake.build()
        # cmake.install()

    def package(self):
        self.copy("*", src="install")
        self.copy("*", dst="bin", src="ITK-prefix/bin")
        self.copy("*", dst="include", src="ITK-prefix/include")
        self.copy("*", dst="lib", src="ITK-prefix/lib")
        self.copy("*", dst="share", src="ITK-prefix/share")

    def package_info(self):
        self.cpp_info.libdirs = ["lib"]
        self.cpp_info.bindirs = ["bin"]
        self.cpp_info.includedirs = ["include/SimpleITK-1.2",
                                     "include/ITK-4.13"]
        self.cpp_info.libs =  tools.collect_libs(self)
