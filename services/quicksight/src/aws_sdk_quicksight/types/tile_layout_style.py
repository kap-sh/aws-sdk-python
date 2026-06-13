"""Generated from Smithy shape ``com.amazonaws.quicksight#TileLayoutStyle``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.gutter_style
    import aws_sdk_quicksight.types.margin_style


class TileLayoutStyle(TypedDict):
    gutter: NotRequired["aws_sdk_quicksight.types.gutter_style.GutterStyle"]
    """<p>The gutter settings that apply between tiles. </p>"""
    margin: NotRequired["aws_sdk_quicksight.types.margin_style.MarginStyle"]
    """<p>The margin settings that apply around the outside edge of sheets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TileLayoutStyle) -> dict:
    out: dict = {}
    if "gutter" in value:
        import aws_sdk_quicksight.types.gutter_style

        out["Gutter"] = aws_sdk_quicksight.types.gutter_style.serialize_json(
            value["gutter"]
        )
    if "margin" in value:
        import aws_sdk_quicksight.types.margin_style

        out["Margin"] = aws_sdk_quicksight.types.margin_style.serialize_json(
            value["margin"]
        )
    return out


def deserialize_json(data: dict) -> TileLayoutStyle:
    out: TileLayoutStyle = {}  # type: ignore[typeddict-item]
    if "Gutter" in data:
        import aws_sdk_quicksight.types.gutter_style

        out["gutter"] = aws_sdk_quicksight.types.gutter_style.deserialize_json(
            data["Gutter"]
        )
    if "Margin" in data:
        import aws_sdk_quicksight.types.margin_style

        out["margin"] = aws_sdk_quicksight.types.margin_style.deserialize_json(
            data["Margin"]
        )
    return out
