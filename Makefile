NAME	:= gotestsum
SRC_EXT	:= gz
VERSION	:= 0.4.0

include packaging/Makefile_packaging.mk

$(VERSION).tar.gz:
	rm -f ./$@
	curl -f -L -O 'https://github.com/gotestyourself/$(NAME)/archive/v$(VERSION).tar.gz'
