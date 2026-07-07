"""Generated from Smithy shape ``com.amazonaws.quicksight#BorderStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.color
    import aws_sdk_quicksight.types.width


class BorderStyle(TypedDict, closed=True):
    color: NotRequired["aws_sdk_quicksight.types.color.Color"]
    """<p>The option to add color for tile borders for visuals.</p>"""
    show: NotRequired["aws_sdk_quicksight.types.boolean.Boolean"]
    """<p>The option to enable display of borders for visuals.</p>"""
    width: NotRequired["aws_sdk_quicksight.types.width.Width"]
    """<p>The option to set the width of tile borders for visuals.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BorderStyle) -> dict:
    out: dict = {}
    if "color" in value:
        out["Color"] = value["color"]
    if "show" in value:
        out["Show"] = value["show"]
    if "width" in value:
        out["Width"] = value["width"]
    return out


def deserialize_json(data: dict) -> BorderStyle:
    out: BorderStyle = {}  # type: ignore[typeddict-item]
    if "Color" in data:
        out["color"] = data["Color"]
    if "Show" in data:
        out["show"] = data["Show"]
    if "Width" in data:
        out["width"] = data["Width"]
    return out
