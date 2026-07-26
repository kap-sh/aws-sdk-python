"""Generated from Smithy shape ``com.amazonaws.quicksight#BorderSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.hex_color_with_transparency
    import capo_quicksight.types.pixel_length
    import capo_quicksight.types.visibility


class BorderSettings(TypedDict, closed=True):
    border_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>Visibility setting for the border.</p>"""
    border_width: NotRequired["capo_quicksight.types.pixel_length.PixelLength"]
    """<p>Width of the border. Valid range is from 1px to 8px.</p>"""
    border_color: NotRequired[
        "capo_quicksight.types.hex_color_with_transparency.HexColorWithTransparency"
    ]
    """<p>Color of the border.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BorderSettings) -> dict:
    out: dict = {}
    if "border_visibility" in value:
        import capo_quicksight.types.visibility

        out["BorderVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["border_visibility"]
        )
    if "border_width" in value:
        out["BorderWidth"] = value["border_width"]
    if "border_color" in value:
        out["BorderColor"] = value["border_color"]
    return out


def deserialize_json(data: dict) -> BorderSettings:
    out: BorderSettings = {}  # type: ignore[typeddict-item]
    if "BorderVisibility" in data:
        import capo_quicksight.types.visibility

        out["border_visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["BorderVisibility"]
        )
    if "BorderWidth" in data:
        out["border_width"] = data["BorderWidth"]
    if "BorderColor" in data:
        out["border_color"] = data["BorderColor"]
    return out
