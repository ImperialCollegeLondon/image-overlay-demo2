# Simple Image Overlay Tool v2

_This repository is one of a pair of repositories being used as part of some
training material that is still under development on research software best
practices._

The Simple Image Overlay Tool (SIOT) is a Python application for overlaying text on an image.

This README provides details on how to run the tool as well as information about contributing to the project and reporting any problems.

### Prerequisites and Dependencies

SIOT requires Python 3.7+.

You will need to have Python installed on your system, it is also recommended that you use a Python virtual environment for installing the dependencies. Ensure you have the `virtualenv` Python package installed to support this.

SIOT makes use of [Pillow](https://pillow.readthedocs.io/en/stable/) a Python imaging library.

### Installation

_NOTE: This is a demonstration tool that is currently not packaged as a Python package. Use of the tool requires a reasonable knowledge of Python environments and the packaging system. These instructions are based on using a CPython (standard system Python installation) on Linux or macOS. Windows users should be able to follow a similar approach but this is currently untested. Likewise, users of Anaconda Python should be able to create a Conda environment and follow a similar approach._

1) Clone the repository from GitHub and create a Python virtual environment in the repository directory:

```
> git clone https://github.com/ImperialCollegeLondon/image-overlay-demo2.git
> cd image-overlay-demo2
> virtualenv env
> source env/bin/activate
```

2) Install the runtime and development dependencies:

```
> pip install -r requirements.txt
```

### Running the tool

Run a test:

A test image file `test_image.jpg` is provided for you to use.

From the `image-overlay-demo2` directory, you can run run `python imgoverlay/imgoverlayapp.py -h` to get help on the various command line options.

Let's add some text to our test image - run the following in the `image-overlay-demo2` directory:

```
> python imgoverlay/imgoverlayapp.py ./test_image.jpg \
  "This text is new!"
```

You should now see a new file in the current directory `test_image_overlay.jpg` that contains the text you specified.

### Highlighting problems

If you identify problems with this tool, please let us know. You can add issues via the ["Issues" link](https://github.com/ImperialCollegeLondon/image-overlay-demo2/issues) in this repository. For bug reports, please complete the bug report template. Please provide as much detail as possible since this will help us to verify and rectify the issue you are reporting.


### Acknowledgements

This tool has been developed as part of training material created to support effective research software development skills. The developer of the material is supported by an EPSRC Research Software Engineering Fellowship Gran