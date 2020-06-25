"""
...
"""
import argparse
import os
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont


def split_slnt(ttfont):
    """Use varlib instance to split a variable font if it contains a
    slnt or ital axis."""
    if 'fvar' not in ttfont:
        raise Exception("Font is not a variable font")

    axes = {a.axisTag: a for a in ttfont['fvar'].axes}
    has_ital = 'ital' in axes
    has_slnt = 'slnt' in axes
    if not any([has_ital, has_slnt]):
        raise Exception("Font does not contain a slnt or ital axis")
    if all([has_ital, has_slnt]):
        raise Exception("Cannot split font which contains both slnt and ital")

    if has_slnt:
        # Use most exteme negative slnt value to make italic
        slnt_angle = axes['slnt'].minValue
        roman = instantiateVariableFont(ttfont, {"slnt": 0})
        italic = instantiateVariableFont(ttfont, {"slnt": slnt_angle})
    else:
        ital_angle = axes['ital'].maxValue
        roman = instantiateVariableFont(ttfont, {"ital": 0})
        italic = instantiateVariableFont(ttfont, {"ital": ital_angle})

    _update_bits(italic)
    _update_nametable(italic)

    roman_filename = os.path.join(
        os.path.dirname(roman.reader.file.name),
        "roman.ttf"
    )
    roman.save(roman_filename)
    italic_filename = os.path.join(
        os.path.dirname(italic.reader.file.name),
        "italic.ttf"
    )
    italic.save(italic_filename)


def _update_bits(ttfont):
    """Update bits for instantiated italic font"""
    # OS/2
    # disable Regular bit and enable italic bit

    # head
    pass


def _update_nametable(ttfont):
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("font")
    args = parser.parse_args()
    ttfont = TTFont(args.font)
    split_slnt(ttfont)


if __name__ == "__main__":
    main()

