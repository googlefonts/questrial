## Fontbakery report

Fontbakery version: 0.8.11

<details><summary><b>[17] Questrial-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Version number has increased since previous release on Google Fonts? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/version_bump">com.google.fonts/check/version_bump</a>)</summary><div>


* 🔥 **FAIL** Version number 2.0 is equal to version on Google Fonts.
* 🔥 **FAIL** Version number 2.0 is equal to version on Google Fonts GitHub repo.
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i᷆ i᷇ ɨ̀ ɨ́ ɨ̂ ɨ̃ ɨ̄ ɨ̈ ɨ̋ ɨ̌ ɨ̏

The dot of soft dotted characters should disappear in other cases, for example: i᷄ i᷅ i̛᷄ i̛᷅ i̛᷆ i̛᷇ i̤᷄ i̤᷅ i̤᷆ i̤᷇ i̥᷄ i̥᷅ i̥᷆ i̥᷇ i̦̍ i̦̐ i̦̓ i̦᷄ i̦᷅ i̦᷆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* arrowdown
	* arrowleft
	* eng.sc
	* exclamdown
	* exclamdown.sc
	* oslash.sc
	* oslashacute.sc
	* triagdn
	* uni0186
	* uni018E
	* uni01A9
	* uni01B8
	* uni01B9
	* uni01C1
	* uni01C3
	* uni0202
	* uni0203
	* uni0203.sc
	* uni0206
	* uni0207
	* uni0207.sc
	* uni020A
	* uni020B
	* uni020B.sc
	* uni020E
	* uni020F
	* uni020F.sc
	* uni0212
	* uni0213
	* uni0213.sc
	* uni0216
	* uni0217
	* uni0217.sc
	* uni0245
	* uni0254
	* uni0295
	* uni02BE
	* uni02BF
	* uni0311
	* uni0311.case
	* uni0312.case
	* uni032F
	* uni1DC5
	* uni1DC6
	* uni25BD and uniA727
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- NULL

	- Ramshorn

	- U1D453

	- eight.sinf

	- eight.subs

	- five.sinf

	- five.subs

	- four.sinf

	- four.subs

	- germandbls.alt.sc

	- macrobelow

	- nine.sinf

	- nine.subs

	- one.sinf

	- one.subs

	- oopenmod

	- seven.sinf

	- seven.subs

	- six.sinf

	- six.subs

	- three.sinf

	- three.subs

	- two.sinf

	- two.subs

	- uni019B.uc

	- uni0220

	- uni025B.mod

	- uni0268.dotless

	- zero.sinf 

	- zero.subs
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 2	Expected: 3 

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 550 among a set of 12 math glyphs.
The following math glyphs have a different width, though:

Width = 593:
logicalnot
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* at (U+0040) contains a short segment B<<543.5,108.0>-<535.0,122.0>-<533.0,132.5>>

	* at (U+0040) contains a short segment B<<533.0,132.5>-<531.0,143.0>-<531.0,143.0>>

	* at (U+0040) contains a short segment B<<597.0,184.0>-<597.0,184.0>-<596.5,180.5>>

	* at (U+0040) contains a short segment B<<596.5,180.5>-<596.0,177.0>-<596.0,171.0>>

	* at (U+0040) contains a short segment B<<596.0,171.0>-<596.0,162.0>-<599.5,149.5>>

	* at (U+0040) contains a short segment B<<599.5,149.5>-<603.0,137.0>-<614.5,127.5>>

	* f (U+0066) contains a short segment L<<290.0,637.0>--<280.0,637.0>>

	* r (U+0072) contains a short segment L<<329.0,433.0>--<320.0,433.0>>

	* Ccedilla (U+00C7) contains a short segment B<<348.0,-50.0>-<360.0,-48.0>-<370.0,-48.0>>

	* eogonek (U+0119) contains a short segment B<<300.0,-8.0>-<293.0,-8.0>-<287.0,-8.0>>

	* Eng (U+014A) contains a short segment L<<577.0,464.0>--<577.0,464.0>>

	* Eng (U+014A) contains a short segment L<<577.0,-21.0>--<577.0,-21.0>>

	* racute (U+0155) contains a short segment L<<329.0,433.0>--<320.0,433.0>>

	* uni0157 (U+0157) contains a short segment L<<329.0,433.0>--<320.0,433.0>>

	* rcaron (U+0159) contains a short segment L<<329.0,433.0>--<320.0,433.0>>

	* longs (U+017F) contains a short segment L<<290.0,637.0>--<280.0,637.0>>

	* uni0187 (U+0187) contains a short segment B<<729.0,789.0>-<737.0,789.0>-<744.0,788.5>>

	* uni0187 (U+0187) contains a short segment B<<744.0,788.5>-<751.0,788.0>-<759.0,787.0>>

	* uni0188 (U+0188) contains a short segment B<<581.0,658.0>-<589.0,658.0>-<596.0,657.5>>

	* uni0188 (U+0188) contains a short segment B<<596.0,657.5>-<603.0,657.0>-<611.0,656.0>>

	* florin (U+0192) contains a short segment B<<29.0,-206.0>-<22.0,-206.0>-<14.5,-205.5>>

	* florin (U+0192) contains a short segment B<<14.5,-205.5>-<7.0,-205.0>-<-1.0,-204.0>>

	* florin (U+0192) contains a short segment L<<290.0,637.0>--<280.0,637.0>>

	* uni0193 (U+0193) contains a short segment B<<729.0,789.0>-<737.0,789.0>-<744.0,788.5>>

	* uni0193 (U+0193) contains a short segment B<<744.0,788.5>-<751.0,788.0>-<759.0,787.0>>

	* uni0193 (U+0193) contains a short segment B<<759.0,719.0>-<746.0,722.0>-<735.0,722.0>>

	* uni0199 (U+0199) contains a short segment B<<210.0,708.0>-<218.0,708.0>-<225.0,707.5>>

	* uni0199 (U+0199) contains a short segment B<<225.0,707.5>-<232.0,707.0>-<240.0,706.0>>

	* uni019D (U+019D) contains a short segment B<<-76.0,-133.0>-<-64.0,-135.0>-<-52.5,-136.0>>

	* uni019D (U+019D) contains a short segment B<<-52.5,-136.0>-<-41.0,-137.0>-<-30.0,-137.0>>

	* uni01A5 (U+01A5) contains a short segment B<<210.0,708.0>-<218.0,708.0>-<225.0,707.5>>

	* uni01A5 (U+01A5) contains a short segment B<<225.0,707.5>-<232.0,707.0>-<240.0,706.0>>

	* uni0211 (U+0211) contains a short segment L<<329.0,433.0>--<320.0,433.0>>

	* uni0213 (U+0213) contains a short segment L<<329.0,433.0>--<320.0,433.0>>

	* uni0228 (U+0228) contains a short segment B<<335.0,-51.0>-<347.0,-49.0>-<357.0,-49.0>>

	* uni0244 (U+0244) contains a short segment L<<636.0,298.0>--<636.0,285.0>>

	* uni024B (U+024B) contains a short segment B<<630.0,-204.0>-<622.0,-205.0>-<615.0,-205.5>>

	* uni024B (U+024B) contains a short segment B<<615.0,-205.5>-<608.0,-206.0>-<600.0,-206.0>>

	* uni024D (U+024D) contains a short segment L<<329.0,433.0>--<320.0,433.0>>

	* uni0253 (U+0253) contains a short segment B<<210.0,707.0>-<218.0,707.0>-<225.0,706.5>>

	* uni0253 (U+0253) contains a short segment B<<225.0,706.5>-<232.0,706.0>-<240.0,705.0>>

	* uni0256 (U+0256) contains a short segment B<<630.0,-204.0>-<622.0,-205.0>-<615.0,-205.5>>

	* uni0256 (U+0256) contains a short segment B<<615.0,-205.5>-<608.0,-206.0>-<600.0,-206.0>>

	* uni0257 (U+0257) contains a short segment B<<600.0,708.0>-<608.0,708.0>-<615.0,707.5>>

	* uni0257 (U+0257) contains a short segment B<<615.0,707.5>-<622.0,707.0>-<630.0,706.0>>

	* uni0260 (U+0260) contains a short segment B<<600.0,708.0>-<608.0,708.0>-<615.0,707.5>>

	* uni0260 (U+0260) contains a short segment B<<615.0,707.5>-<622.0,707.0>-<630.0,706.0>>

	* uni0266 (U+0266) contains a short segment B<<210.0,708.0>-<218.0,708.0>-<225.0,707.5>>

	* uni0266 (U+0266) contains a short segment B<<225.0,707.5>-<232.0,707.0>-<240.0,706.0>>

	* uni026C (U+026C) contains a short segment L<<148.0,298.0>--<137.0,298.0>>

	* uni0272 (U+0272) contains a short segment B<<-5.0,-206.0>-<-12.0,-206.0>-<-19.5,-205.5>>

	* uni0272 (U+0272) contains a short segment B<<-19.5,-205.5>-<-27.0,-205.0>-<-35.0,-204.0>>

	* rtail (U+027D) contains a short segment L<<329.0,433.0>--<320.0,433.0>>

	* uni0283 (U+0283) contains a short segment L<<290.0,637.0>--<280.0,637.0>>

	* uni0283 (U+0283) contains a short segment L<<-17.0,-127.0>--<-7.0,-127.0>>

	* uni1DCA (U+1DCA) contains a short segment L<<169.0,-89.0>--<164.0,-89.0>>

	* uni1E08 (U+1E08) contains a short segment B<<348.0,-50.0>-<360.0,-48.0>-<370.0,-48.0>>

	* uni1E1C (U+1E1C) contains a short segment B<<335.0,-51.0>-<347.0,-49.0>-<357.0,-49.0>>

	* uni1E1F (U+1E1F) contains a short segment L<<290.0,637.0>--<280.0,637.0>>

	* uni1E59 (U+1E59) contains a short segment L<<329.0,433.0>--<320.0,433.0>>

	* uni1E5B (U+1E5B) contains a short segment L<<329.0,433.0>--<320.0,433.0>>

	* uni1E5D (U+1E5D) contains a short segment L<<329.0,433.0>--<320.0,433.0>>

	* rmacronbelow (U+1E5F) contains a short segment L<<329.0,433.0>--<320.0,433.0>>

	* uni1E9E (U+1E9E) contains a short segment L<<394.0,355.0>--<415.0,355.0>>

	* colonmonetary (U+20A1) contains a short segment B<<329.0,65.0>-<337.0,65.0>-<345.0,65.0>>

	* lira (U+20A4) contains a short segment B<<99.0,445.0>-<98.0,453.0>-<97.5,462.5>>

	* lira (U+20A4) contains a short segment B<<97.5,462.5>-<97.0,472.0>-<97.0,482.0>>

	* lira (U+20A4) contains a short segment B<<178.0,474.0>-<178.0,467.0>-<178.5,460.0>>

	* lira (U+20A4) contains a short segment B<<178.5,460.0>-<179.0,453.0>-<180.0,445.0>>

	* uni20A9 (U+20A9) contains a short segment L<<356.0,661.0>--<355.0,662.0>>

	* Euro (U+20AC) contains a short segment B<<126.0,306.0>-<125.0,313.0>-<125.0,319.0>>

	* Euro (U+20AC) contains a short segment B<<125.0,319.0>-<125.0,325.0>-<125.0,331.0>>

	* Euro (U+20AC) contains a short segment B<<125.0,331.0>-<125.0,342.0>-<125.5,353.5>>

	* Euro (U+20AC) contains a short segment B<<125.5,353.5>-<126.0,365.0>-<127.0,375.0>>

	* Euro (U+20AC) contains a short segment B<<202.0,375.0>-<201.0,365.0>-<200.5,353.5>>

	* Euro (U+20AC) contains a short segment B<<200.5,353.5>-<200.0,342.0>-<200.0,331.0>>

	* Euro (U+20AC) contains a short segment B<<200.0,331.0>-<200.0,325.0>-<200.0,319.0>>

	* Euro (U+20AC) contains a short segment B<<200.0,319.0>-<200.0,313.0>-<201.0,306.0>>

	* uni20B1 (U+20B1) contains a short segment B<<556.0,459.0>-<557.0,452.0>-<557.0,444.5>>

	* estimated (U+212E) contains a short segment B<<167.0,303.0>-<161.0,303.0>-<161.0,299.0>>

	* estimated (U+212E) contains a short segment B<<615.0,322.0>-<619.0,322.0>-<619.0,327.0>>

	* uniA726 (U+A726) contains a short segment B<<384.0,-133.0>-<396.0,-135.0>-<407.5,-136.0>>

	* uniA726 (U+A726) contains a short segment B<<407.5,-136.0>-<419.0,-137.0>-<430.0,-137.0>>

	* uniA7AA (U+A7AA) contains a short segment B<<74.0,479.0>-<74.0,468.0>-<75.0,456.5>>

	* uniA7AA (U+A7AA) contains a short segment B<<75.0,456.5>-<76.0,445.0>-<78.0,433.0>>

	* f_f (U+FB00) contains a short segment L<<290.0,637.0>--<280.0,637.0>>

	* f_f (U+FB00) contains a short segment L<<587.0,637.0>--<577.0,637.0>>

	* fi (U+FB01) contains a short segment L<<290.0,637.0>--<280.0,637.0>>

	* fi (U+FB01) contains a short segment L<<431.0,500.0>--<429.0,498.0>>

	* fl (U+FB02) contains a short segment L<<290.0,637.0>--<280.0,637.0>>

	* f_f_i (U+FB03) contains a short segment L<<290.0,637.0>--<280.0,637.0>>

	* f_f_i (U+FB03) contains a short segment L<<587.0,637.0>--<577.0,637.0>>

	* f_f_l (U+FB04) contains a short segment L<<290.0,637.0>--<280.0,637.0>> 

	* f_f_l (U+FB04) contains a short segment L<<587.0,637.0>--<577.0,637.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* lambda (U+03BB): L<<276.0,556.0>--<318.0,456.0>> -> L<<318.0,456.0>--<457.0,128.0>> 

	* uni019B (U+019B): L<<276.0,556.0>--<318.0,456.0>> -> L<<318.0,456.0>--<457.0,128.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* uni0280 (U+0280): L<<140.0,253.0>--<260.0,252.0>> [code: found-semi-vertical]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 5 | 12 | 115 | 8 | 102 | 0 |
| 0% | 2% | 5% | 48% | 3% | 42% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
