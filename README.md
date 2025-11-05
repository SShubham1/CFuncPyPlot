# CFuncPyPlot
## C Computation 🖥️ x Python Visualization 📊

[![Build Status](https://img.shields.io/github/actions/workflow/status/SShubham1/CFuncPyPlot/build.yml?branch=master)](https://github.com/SShubham1/CFuncPyPlot/actions)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A small project demonstrating how to generate arrays of function values in C, expose them as a shared library, and plot them in Python using `matplotlib`.

---

## Features ✨

- C library that generates `x` and `y` arrays for various functions.
- Python script to plot the data.
- Cross-platform support: Linux, macOS, Windows.
- CMake-based build system.
- Ready for GitHub Actions CI/CD.

---

## Project Structure 📁

```
CFuncPyPlot/
├─ function_data.c       # C code generating function arrays
├─ plot_data.py          # Python script to plot arrays
├─ CMakeLists.txt        # Build configuration
├─ .gitignore
├─ README.md
└─ .github/
   └─ workflows/
      └─ build.yml       # CI/CD workflow
```

---

## Build Instructions 🛠️

### 1. Install dependencies

- **Linux**: `sudo apt-get install build-essential cmake python3 python3-pip`
- **macOS**: `brew install cmake python3` (Xcode CLI tools required)
- **Windows**: Install [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

### 2. Clone the repository

```
bash
git clone https://github.com/SShubham1/CFuncPyPlot.git
cd CFuncPyPlot
```

### 3. Build with CMake

```
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

- The shared library and `plot_data.py` will be in `build/release/`.

### 4. Run the Python script 🐍

```
cd release
python plot_data.py
```

---

### Supported Functions 🔢

You can modify `y_array()` in `function_data.c` to use:

```
y_arr[i] = (i*0.01)*(i*0.01);     // x^2
y_arr[i] = sin(i*0.01);           // sin(x)
y_arr[i] = log(i*0.01);           // ln(x)
y_arr[i] = i*0.01;                // linear
y_arr[i] = cos(i*0.01);           // cos(x)
```

### License 📝


This project is licensed under the [MIT License](LICENSE).

