Import("env")

env.Replace(CC="gcc-10", CXX="g++-10")

env.Replace(BUILD_SCRIPT="tools/osx_build_script.py")

#print('=====================================')
#print(env.Dump())
