# source venv/bin/activate
set -e

mkdir -p ../fonts ../fonts/ttf ../fonts/otf ../fonts/woff2

echo "GENERATING TTFs"
fontmake -g Questrial.glyphs -i -o ttf --output-dir ../fonts/ttf/

echo "POST PROCESSING TTFs"
ttfs=$(ls ../fonts/ttf/*.ttf)
for ttf in $ttfs
do
	ttfautohint $ttf "$ttf.fix";
	mv "$ttf.fix" $ttf;

    gftools fix-hinting $ttf;
    mv "$ttf.fix" $ttf;

    gftools fix-dsig -f $ttf;
done

echo "GENERATING WOFFs"
ttfs=$(ls ../fonts/*/*.ttf)
for ttf in $ttfs; do
    woff2_compress $ttf
done

woff2s=$(ls ../fonts/*/*.woff2)
for woff2 in $woff2s; do
    mv $woff2 ../fonts/woff2/$(basename $woff2)
done


echo "GENERATING OTFs"
fontmake -g Questrial.glyphs -i -o otf --output-dir ../fonts/otf/

echo "POST PROCESSING OTFs"
otfs=$(ls ../fonts/otf/*.otf)
for otf in $otfs
do
    gftools fix-dsig -f $otf;
    psautohint $otf;
done

rm -rf master_ufo/ instance_ufo/

