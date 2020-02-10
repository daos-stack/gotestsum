NAME         := gotestsum
SRC_EXT      := gz
MOCK_OPTIONS := --enable-network # needed to download modules

include packaging/Makefile_packaging.mk

clean:
	git clean -dfx .
