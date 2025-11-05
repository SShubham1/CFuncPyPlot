cmake_minimum_required(VERSION 3.10)
project(CFuncPyPlot LANGUAGES C)

# Create shared library
add_library(function_data SHARED function_data.c)

# Link math library on Linux/macOS
if(UNIX)
    target_link_libraries(function_data m)
endif()

# Set the output folder to a single "release" folder
set_target_properties(function_data PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/release    # Windows DLL
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/release    # Linux/macOS .so/.dylib
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/release    # static libs
)

# Copy Python script into the same folder
file(COPY ${CMAKE_SOURCE_DIR}/plot_data.py
     DESTINATION ${CMAKE_BINARY_DIR}/release)

add_custom_command(TARGET function_data POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E echo "Release files are in ${CMAKE_BINARY_DIR}/release"
)

