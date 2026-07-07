"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#HorizontalLayoutConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.horizontal_tile_position
    import aws_sdk_chime_sdk_media_pipelines.types.tile_aspect_ratio
    import aws_sdk_chime_sdk_media_pipelines.types.tile_count
    import aws_sdk_chime_sdk_media_pipelines.types.tile_order


class HorizontalLayoutConfiguration(TypedDict, closed=True):
    tile_order: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.tile_order.TileOrder"
    ]
    """<p>Sets the automatic ordering of the video tiles.</p>"""
    tile_position: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.horizontal_tile_position.HorizontalTilePosition"
    ]
    """<p>Sets the position of horizontal tiles.</p>"""
    tile_count: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.tile_count.TileCount"
    ]
    """<p>The maximum number of video tiles to display.</p>"""
    tile_aspect_ratio: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.tile_aspect_ratio.TileAspectRatio"
    ]
    """<p>Specifies the aspect ratio of all video tiles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HorizontalLayoutConfiguration) -> dict:
    out: dict = {}
    if "tile_order" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.tile_order

        out["TileOrder"] = (
            aws_sdk_chime_sdk_media_pipelines.types.tile_order.serialize_json(
                value["tile_order"]
            )
        )
    if "tile_position" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.horizontal_tile_position

        out["TilePosition"] = (
            aws_sdk_chime_sdk_media_pipelines.types.horizontal_tile_position.serialize_json(
                value["tile_position"]
            )
        )
    if "tile_count" in value:
        out["TileCount"] = value["tile_count"]
    if "tile_aspect_ratio" in value:
        out["TileAspectRatio"] = value["tile_aspect_ratio"]
    return out


def deserialize_json(data: dict) -> HorizontalLayoutConfiguration:
    out: HorizontalLayoutConfiguration = {}  # type: ignore[typeddict-item]
    if "TileOrder" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.tile_order

        out["tile_order"] = (
            aws_sdk_chime_sdk_media_pipelines.types.tile_order.deserialize_json(
                data["TileOrder"]
            )
        )
    if "TilePosition" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.horizontal_tile_position

        out["tile_position"] = (
            aws_sdk_chime_sdk_media_pipelines.types.horizontal_tile_position.deserialize_json(
                data["TilePosition"]
            )
        )
    if "TileCount" in data:
        out["tile_count"] = data["TileCount"]
    if "TileAspectRatio" in data:
        out["tile_aspect_ratio"] = data["TileAspectRatio"]
    return out
