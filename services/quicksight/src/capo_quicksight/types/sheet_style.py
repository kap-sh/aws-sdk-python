"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.sheet_background_style
    import capo_quicksight.types.tile_layout_style
    import capo_quicksight.types.tile_style


class SheetStyle(TypedDict, closed=True):
    tile: NotRequired["capo_quicksight.types.tile_style.TileStyle"]
    """<p>The display options for tiles.</p>"""
    tile_layout: NotRequired["capo_quicksight.types.tile_layout_style.TileLayoutStyle"]
    """<p>The layout options for tiles.</p>"""
    background: NotRequired[
        "capo_quicksight.types.sheet_background_style.SheetBackgroundStyle"
    ]
    """<p>The background for sheets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetStyle) -> dict:
    out: dict = {}
    if "tile" in value:
        import capo_quicksight.types.tile_style

        out["Tile"] = capo_quicksight.types.tile_style.serialize_json(value["tile"])
    if "tile_layout" in value:
        import capo_quicksight.types.tile_layout_style

        out["TileLayout"] = capo_quicksight.types.tile_layout_style.serialize_json(
            value["tile_layout"]
        )
    if "background" in value:
        import capo_quicksight.types.sheet_background_style

        out["Background"] = capo_quicksight.types.sheet_background_style.serialize_json(
            value["background"]
        )
    return out


def deserialize_json(data: dict) -> SheetStyle:
    out: SheetStyle = {}  # type: ignore[typeddict-item]
    if "Tile" in data:
        import capo_quicksight.types.tile_style

        out["tile"] = capo_quicksight.types.tile_style.deserialize_json(data["Tile"])
    if "TileLayout" in data:
        import capo_quicksight.types.tile_layout_style

        out["tile_layout"] = capo_quicksight.types.tile_layout_style.deserialize_json(
            data["TileLayout"]
        )
    if "Background" in data:
        import capo_quicksight.types.sheet_background_style

        out["background"] = (
            capo_quicksight.types.sheet_background_style.deserialize_json(
                data["Background"]
            )
        )
    return out
