#!/bin/bash

set -e
tempDir=$(mktemp -d)
checkoutDir="$tempDir/rtags"
git clone --quiet https://github.com/Andersbakken/rtags "$checkoutDir"
(cd "$checkoutDir"; git submodule --quiet init; git submodule --quiet update)
tar -C "$tempDir" -cjf rtags.tar.bz2 rtags

lastTag=$(cd "$checkoutDir"; git describe --tags --abbrev=0 | sed 's/^v//')
headCommit=$(cd "$checkoutDir"; git rev-list HEAD -n 1 | cut -c 1-7)

echo "%global gitdate $(date +%Y%m%d)"
echo "%global gitversion ${lastTag}"
echo "%global gitcommit ${headCommit}"

rm -rf "$tempDir"
