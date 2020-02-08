NAME	:= gotestsum
SRC_EXT	:= gz

include packaging/Makefile_packaging.mk

clean:
	git clean -dfx .
