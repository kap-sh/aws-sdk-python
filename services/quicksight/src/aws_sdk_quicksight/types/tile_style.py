"""Generated from Smithy shape ``com.amazonaws.quicksight#TileStyle``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.border_radius
    import aws_sdk_quicksight.types.border_style
    import aws_sdk_quicksight.types.color
    import aws_sdk_quicksight.types.padding


class TileStyle(TypedDict):
    background_color: NotRequired["aws_sdk_quicksight.types.color.Color"]
    """<p>The background color of a tile.</p>"""
    border: NotRequired["aws_sdk_quicksight.types.border_style.BorderStyle"]
    """<p>The border around a tile.</p>"""
    border_radius: NotRequired["aws_sdk_quicksight.types.border_radius.BorderRadius"]
    """<p>The border radius of a tile.</p>"""
    padding: NotRequired["aws_sdk_quicksight.types.padding.Padding"]
    """<p>The padding of a tile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TileStyle) -> dict:
    out: dict = {}
    if "background_color" in value:
        out["BackgroundColor"] = value["background_color"]
    if "border" in value:
        import aws_sdk_quicksight.types.border_style

        out["Border"] = aws_sdk_quicksight.types.border_style.serialize_json(
            value["border"]
        )
    if "border_radius" in value:
        out["BorderRadius"] = value["border_radius"]
    if "padding" in value:
        out["Padding"] = value["padding"]
    return out


def deserialize_json(data: dict) -> TileStyle:
    out: TileStyle = {}  # type: ignore[typeddict-item]
    if "BackgroundColor" in data:
        out["background_color"] = data["BackgroundColor"]
    if "Border" in data:
        import aws_sdk_quicksight.types.border_style

        out["border"] = aws_sdk_quicksight.types.border_style.deserialize_json(
            data["Border"]
        )
    if "BorderRadius" in data:
        out["border_radius"] = data["BorderRadius"]
    if "Padding" in data:
        out["padding"] = data["Padding"]
    return out
