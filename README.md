[![Build status](https://ci.appveyor.com/api/projects/status/3li2lfv25ebnq1xg?svg=true)](https://ci.appveyor.com/project/AtaLuZiK/conan-rapidjson)
[![Build status](https://ci.appveyor.com/api/projects/status/3li2lfv25ebnq1xg?svg=true)](https://ci.appveyor.com/project/AtaLuZiK/conan-rapidjson)

# conan-rapidjson

Conan package for [rapidjson](https://github.com/Tencent/rapidjson)

The packages generated with this **conanfile** can be found on [bintray](https://bintray.com/conan-community).

## Reuse the packages

### Basic setup

```
conan install rapidjson/1.1.0@zimmerk/stable
```

### Project setup

```
[requires]
rapidjson/1.1.0@zimmerk/stable

[options]
# Take a look for all avaliable options in conanfile.py

[generators]
cmake
```

Complete the installitation of requirements for your project running:

```
conan install .
```

Project setup installs the library (and all his dependencies) and generates the files conanbuildinfo.txt and conanbuildinfo.cmake with all the paths and variables that you need to link with your dependencies.

Follow the Conan getting started: http://docs.conan.io