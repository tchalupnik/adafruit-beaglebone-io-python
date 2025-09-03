# Default target
all: cpp

# Sync system time (if needed for development)
time:
	/usr/bin/ntpdate -b -s -u pool.ntp.org

################################################################################
# C++ library
#
# Prerequisites:
# sudo apt-get install automake autoconf libtool libgtest-dev
#
# Usage for BeagleBone setup:
# sudo sh -c 'echo cape-universaln > /sys/devices/platform/bone_capemgr/slots'
# sudo sh -c 'echo pwm > /sys/devices/platform/ocp/ocp\:P9_16_pinmux/state'
# sudo sh -c 'echo pwm > /sys/devices/platform/ocp/ocp\:P8_19_pinmux/state'
################################################################################

configure: configure.ac
	rm -f configure && \
	autoreconf --install -I m4

build/Makefile: configure
	mkdir -p build && \
	cd build && \
	../configure

cpp: build/Makefile
	cd build && \
	$(MAKE) build

cpp-test: cpp
	cd build && \
	$(MAKE) check

cpp-install: cpp
	cd build && \
	sudo $(MAKE) install

cpp-clean:
	rm -rf build/ \
	  Makefile.in \
	  aclocal.m4 \
	  autom4te.cache/ \
	  compile \
	  configure \
	  config.guess \
	  config.h.in \
	  config.sub \
	  depcomp \
	  install-sh \
	  ltmain.sh \
	  m4/libtool.m4 \
	  m4/ltoptions.m4 \
	  m4/ltsugar.m4 \
	  m4/ltversion.m4 \
	  m4/lt~obsolete.m4 \
	  missing \
	  source/Makefile.in \
	  test-driver

# Clean everything
clean: cpp-clean

# Define phony targets
.PHONY: all time cpp cpp-test cpp-install cpp-clean configure clean
