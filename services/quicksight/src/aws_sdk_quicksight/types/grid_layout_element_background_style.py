"""Generated from Smithy shape ``com.amazonaws.quicksight#GridLayoutElementBackgroundStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.hex_color_with_transparency
    import aws_sdk_quicksight.types.visibility


class GridLayoutElementBackgroundStyle(TypedDict, closed=True):
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The background visibility of a grid layout element.</p>"""
    color: NotRequired[
        "aws_sdk_quicksight.types.hex_color_with_transparency.HexColorWithTransparency"
    ]
    """<p>The background color of a grid layout element.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GridLayoutElementBackgroundStyle) -> dict:
    out: dict = {}
    if "visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["Visibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "color" in value:
        out["Color"] = value["color"]
    return out


def deserialize_json(data: dict) -> GridLayoutElementBackgroundStyle:
    out: GridLayoutElementBackgroundStyle = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "Color" in data:
        out["color"] = data["Color"]
    return out
