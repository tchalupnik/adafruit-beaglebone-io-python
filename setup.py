import io
import platform
from setuptools import setup, Extension, find_packages

# Compile and copy overlays if possible
try:
    from overlays import builder

    builder.compile()
    builder.copy()
except ImportError:
    pass


def open_as_utf8(filename):
    """Open file with UTF-8 encoding."""
    return io.open(filename, encoding="utf-8")


kernel = platform.release()

if kernel >= "4.1.0":
    kernel41 = [("BBBVERSION41", None)]
else:
    kernel41 = None

CFLAGS = ["-Wall"]

classifiers = [
    "Development Status :: 4 - Beta",
    "Operating System :: POSIX :: Linux",
    "License :: OSI Approved :: MIT License",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Topic :: Software Development",
    "Topic :: Home Automation",
    "Topic :: System :: Hardware",
]

extension_args = {
    "include_dirs": ["source/include/"],
    "extra_compile_args": CFLAGS,
    "define_macros": kernel41,
}

setup(
    name="Adafruit_BBIO",
    version="1.2.0",
    author="Justin Cooper",
    author_email="justin@adafruit.com",
    description="A module to control BeagleBone IO channels",
    long_description=open_as_utf8("README.md").read()
    + open_as_utf8("CHANGELOG.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="Adafruit BeagleBone IO GPIO PWM ADC",
    url="https://github.com/adafruit/adafruit-beaglebone-io-python/",
    classifiers=classifiers,
    packages=find_packages(),
    py_modules=["Adafruit_I2C"],
    python_requires=">=3.10",
    ext_modules=[
        Extension(
            "Adafruit_BBIO.GPIO",
            [
                "source/py_gpio.c",
                "source/event_gpio.c",
                "source/c_pinmux.c",
                "source/constants.c",
                "source/common.c",
            ],
            **extension_args,
        ),
        Extension(
            "Adafruit_BBIO.PWM",
            [
                "source/py_pwm.c",
                "source/c_pwm.c",
                "source/c_pinmux.c",
                "source/constants.c",
                "source/common.c",
            ],
            **extension_args,
        ),
        Extension(
            "Adafruit_BBIO.ADC",
            [
                "source/py_adc.c",
                "source/c_adc.c",
                "source/constants.c",
                "source/common.c",
            ],
            **extension_args,
        ),
        Extension(
            "Adafruit_BBIO.SPI",
            [
                "source/spimodule.c",
                "source/c_pinmux.c",
                "source/constants.c",
                "source/common.c",
            ],
            **extension_args,
        ),
        Extension(
            "Adafruit_BBIO.UART",
            [
                "source/py_uart.c",
                "source/c_pinmux.c",
                "source/c_uart.c",
                "source/constants.c",
                "source/common.c",
            ],
            **extension_args,
        ),
    ],
)
