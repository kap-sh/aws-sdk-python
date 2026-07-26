"""Generated from Smithy shape ``com.amazonaws.medialive#EbuTtDDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min1_max800
    import capo_medialive.types.__integer_min80_max800
    import capo_medialive.types.__string
    import capo_medialive.types.__string_max1000
    import capo_medialive.types.ebu_tt_d_destination_style_control
    import capo_medialive.types.ebu_tt_d_fill_line_gap_control


class EbuTtDDestinationSettings(TypedDict, closed=True):
    copyright_holder: NotRequired[
        "capo_medialive.types.__string_max1000.__stringMax1000"
    ]
    """Complete this field if you want to include the name of the copyright holder in the copyright tag in the captions metadata."""
    fill_line_gap: NotRequired[
        "capo_medialive.types.ebu_tt_d_fill_line_gap_control.EbuTtDFillLineGapControl"
    ]
    """Specifies how to handle the gap between the lines (in multi-line captions). ENABLED: Fill with the captions background color (as specified in the input captions). DISABLED: Leave the gap unfilled"""
    font_family: NotRequired["capo_medialive.types.__string.__string"]
    """Specifies the font family to include in the font data attached to the EBU-TT captions. Valid only if style_control is set to include. (If style_control is set to exclude, the font family is always set to monospaced.) Enter a list of font families, as a comma-separated list of font names, in order of preference. The name can be a font family (such as Arial), or a generic font family (such as serif), or default (to let the downstream player choose the font). Or leave blank to set the family to monospace. Note that you can specify only the font family. All other style information (color, bold, position and so on) is copied from the input captions. The size is always set to 100% to allow the downstream player to choose the size."""
    style_control: NotRequired[
        "capo_medialive.types.ebu_tt_d_destination_style_control.EbuTtDDestinationStyleControl"
    ]
    """Specifies the style information to include in the font data that is attached to the EBU-TT captions. INCLUDE: Take the style information from the source captions and include that information in the font data attached to the EBU-TT captions. This option is valid only if the source captions are Embedded or Teletext. EXCLUDE: Set the font family to monospaced. Do not include any other style information."""
    default_font_size: NotRequired[
        "capo_medialive.types.__integer_min1_max800.__integerMin1Max800"
    ]
    """Specifies the default font size as a percentage of the computed cell size. Valid only if the defaultLineHeight is also set. If you leave this field empty, the default font size is 80% of the cell size."""
    default_line_height: NotRequired[
        "capo_medialive.types.__integer_min80_max800.__integerMin80Max800"
    ]
    """Documentation update needed"""


# --- restJson1 ser/de ---
def serialize_json(value: EbuTtDDestinationSettings) -> dict:
    out: dict = {}
    if "copyright_holder" in value:
        out["copyrightHolder"] = value["copyright_holder"]
    if "fill_line_gap" in value:
        import capo_medialive.types.ebu_tt_d_fill_line_gap_control

        out["fillLineGap"] = (
            capo_medialive.types.ebu_tt_d_fill_line_gap_control.serialize_json(
                value["fill_line_gap"]
            )
        )
    if "font_family" in value:
        out["fontFamily"] = value["font_family"]
    if "style_control" in value:
        import capo_medialive.types.ebu_tt_d_destination_style_control

        out["styleControl"] = (
            capo_medialive.types.ebu_tt_d_destination_style_control.serialize_json(
                value["style_control"]
            )
        )
    if "default_font_size" in value:
        out["defaultFontSize"] = value["default_font_size"]
    if "default_line_height" in value:
        out["defaultLineHeight"] = value["default_line_height"]
    return out


def deserialize_json(data: dict) -> EbuTtDDestinationSettings:
    out: EbuTtDDestinationSettings = {}  # type: ignore[typeddict-item]
    if "copyrightHolder" in data:
        out["copyright_holder"] = data["copyrightHolder"]
    if "fillLineGap" in data:
        import capo_medialive.types.ebu_tt_d_fill_line_gap_control

        out["fill_line_gap"] = (
            capo_medialive.types.ebu_tt_d_fill_line_gap_control.deserialize_json(
                data["fillLineGap"]
            )
        )
    if "fontFamily" in data:
        out["font_family"] = data["fontFamily"]
    if "styleControl" in data:
        import capo_medialive.types.ebu_tt_d_destination_style_control

        out["style_control"] = (
            capo_medialive.types.ebu_tt_d_destination_style_control.deserialize_json(
                data["styleControl"]
            )
        )
    if "defaultFontSize" in data:
        out["default_font_size"] = data["defaultFontSize"]
    if "defaultLineHeight" in data:
        out["default_line_height"] = data["defaultLineHeight"]
    return out
