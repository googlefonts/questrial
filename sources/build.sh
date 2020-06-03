#!/bin/sh
set -e

rm -rf ../fonts
mkdir -p ../fonts/{ttf,otf}
glyphs=$(ls *.glyphs)

echo "Generating static fonts"
for glyph in $glyphs
do
	fontmake -g $glyph -o variable -i -o ttf --output-dir ../fonts/ttf/
	fontmake -g $glyph -o variable -i -o otf --output-dir ../fonts/otf/
done

rm -rf master_ufo/ instance_ufo/
