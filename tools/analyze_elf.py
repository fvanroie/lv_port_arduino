Import("env")

# Add custom target to explorer
env.AddTarget(
    name = "analyze_ram",
    dependencies = "$BUILD_DIR\${PROGNAME}${PROGSUFFIX}",
    actions = 'python $PROJECT_DIR/tools/elf-size-analyze.py $BUILD_DIR\${PROGNAME}${PROGSUFFIX} -t $PROJECT_PACKAGES_DIR\\toolchain-xtensa32\\bin\\xtensa-esp32-elf- -a -H -w 120 -R -m 512',
    title = "Analyze RAM",
    description = "Build and analyze",
    group="Analyze"
)
env.AddTarget(
    name = "analyze_flash",
    dependencies = "$BUILD_DIR\${PROGNAME}${PROGSUFFIX}",
    actions = 'python $PROJECT_DIR/tools/elf-size-analyze.py $BUILD_DIR\${PROGNAME}${PROGSUFFIX} -t $PROJECT_PACKAGES_DIR\\toolchain-xtensa32\\bin\\xtensa-esp32-elf- -a -H -w 120 -F -m 512',
    title = "Analyze Flash",
    description = "Build and analyze",
    group="Analyze"
)


print('=====================================')
