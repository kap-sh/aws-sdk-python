"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#VerticalLayoutConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.tile_aspect_ratio
    import aws_sdk_chime_sdk_media_pipelines.types.tile_count
    import aws_sdk_chime_sdk_media_pipelines.types.tile_order
    import aws_sdk_chime_sdk_media_pipelines.types.vertical_tile_position


class VerticalLayoutConfiguration(TypedDict):
    tile_order: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.tile_order.TileOrder"
    ]
    """<p>Sets the automatic ordering of the video tiles.</p>"""
    tile_position: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.vertical_tile_position.VerticalTilePosition"
    ]
    """<p>Sets the position of vertical tiles.</p>"""
    tile_count: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.tile_count.TileCount"
    ]
    """<p>The maximum number of tiles to display.</p>"""
    tile_aspect_ratio: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.tile_aspect_ratio.TileAspectRatio"
    ]
    """<p>Sets the aspect ratio of the video tiles, such as 16:9.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerticalLayoutConfiguration) -> dict:
    out: dict = {}
    if "tile_order" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.tile_order

        out["TileOrder"] = (
            aws_sdk_chime_sdk_media_pipelines.types.tile_order.serialize_json(
                value["tile_order"]
            )
        )
    if "tile_position" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.vertical_tile_position

        out["TilePosition"] = (
            aws_sdk_chime_sdk_media_pipelines.types.vertical_tile_position.serialize_json(
                value["tile_position"]
            )
        )
    if "tile_count" in value:
        out["TileCount"] = value["tile_count"]
    if "tile_aspect_ratio" in value:
        out["TileAspectRatio"] = value["tile_aspect_ratio"]
    return out


def deserialize_json(data: dict) -> VerticalLayoutConfiguration:
    out: VerticalLayoutConfiguration = {}  # type: ignore[typeddict-item]
    if "TileOrder" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.tile_order

        out["tile_order"] = (
            aws_sdk_chime_sdk_media_pipelines.types.tile_order.deserialize_json(
                data["TileOrder"]
            )
        )
    if "TilePosition" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.vertical_tile_position

        out["tile_position"] = (
            aws_sdk_chime_sdk_media_pipelines.types.vertical_tile_position.deserialize_json(
                data["TilePosition"]
            )
        )
    if "TileCount" in data:
        out["tile_count"] = data["TileCount"]
    if "TileAspectRatio" in data:
        out["tile_aspect_ratio"] = data["TileAspectRatio"]
    return out
