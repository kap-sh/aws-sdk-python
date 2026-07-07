"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sheet_background_style
    import aws_sdk_quicksight.types.tile_layout_style
    import aws_sdk_quicksight.types.tile_style


class SheetStyle(TypedDict, closed=True):
    tile: NotRequired["aws_sdk_quicksight.types.tile_style.TileStyle"]
    """<p>The display options for tiles.</p>"""
    tile_layout: NotRequired[
        "aws_sdk_quicksight.types.tile_layout_style.TileLayoutStyle"
    ]
    """<p>The layout options for tiles.</p>"""
    background: NotRequired[
        "aws_sdk_quicksight.types.sheet_background_style.SheetBackgroundStyle"
    ]
    """<p>The background for sheets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetStyle) -> dict:
    out: dict = {}
    if "tile" in value:
        import aws_sdk_quicksight.types.tile_style

        out["Tile"] = aws_sdk_quicksight.types.tile_style.serialize_json(value["tile"])
    if "tile_layout" in value:
        import aws_sdk_quicksight.types.tile_layout_style

        out["TileLayout"] = aws_sdk_quicksight.types.tile_layout_style.serialize_json(
            value["tile_layout"]
        )
    if "background" in value:
        import aws_sdk_quicksight.types.sheet_background_style

        out["Background"] = (
            aws_sdk_quicksight.types.sheet_background_style.serialize_json(
                value["background"]
            )
        )
    return out


def deserialize_json(data: dict) -> SheetStyle:
    out: SheetStyle = {}  # type: ignore[typeddict-item]
    if "Tile" in data:
        import aws_sdk_quicksight.types.tile_style

        out["tile"] = aws_sdk_quicksight.types.tile_style.deserialize_json(data["Tile"])
    if "TileLayout" in data:
        import aws_sdk_quicksight.types.tile_layout_style

        out["tile_layout"] = (
            aws_sdk_quicksight.types.tile_layout_style.deserialize_json(
                data["TileLayout"]
            )
        )
    if "Background" in data:
        import aws_sdk_quicksight.types.sheet_background_style

        out["background"] = (
            aws_sdk_quicksight.types.sheet_background_style.deserialize_json(
                data["Background"]
            )
        )
    return out
