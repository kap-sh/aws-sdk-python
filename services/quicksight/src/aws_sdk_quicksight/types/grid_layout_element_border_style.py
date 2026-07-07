"""Generated from Smithy shape ``com.amazonaws.quicksight#GridLayoutElementBorderStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.hex_color_with_transparency
    import aws_sdk_quicksight.types.visibility
    import aws_sdk_quicksight.types.width


class GridLayoutElementBorderStyle(TypedDict, closed=True):
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The border visibility of a grid layout element.</p>"""
    color: NotRequired[
        "aws_sdk_quicksight.types.hex_color_with_transparency.HexColorWithTransparency"
    ]
    """<p>The border color of a grid layout element.</p>"""
    width: NotRequired["aws_sdk_quicksight.types.width.Width"]
    """<p>The border width of a grid layout element.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GridLayoutElementBorderStyle) -> dict:
    out: dict = {}
    if "visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["Visibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "color" in value:
        out["Color"] = value["color"]
    if "width" in value:
        out["Width"] = value["width"]
    return out


def deserialize_json(data: dict) -> GridLayoutElementBorderStyle:
    out: GridLayoutElementBorderStyle = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "Color" in data:
        out["color"] = data["Color"]
    if "Width" in data:
        out["width"] = data["Width"]
    return out
