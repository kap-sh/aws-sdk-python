"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsImageBasedTrickPlaySettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__double_min0_max2147483647
    import aws_sdk_mediaconvert.types.__integer_min1_max512
    import aws_sdk_mediaconvert.types.__integer_min1_max2048
    import aws_sdk_mediaconvert.types.__integer_min2_max4096
    import aws_sdk_mediaconvert.types.__integer_min8_max4096
    import aws_sdk_mediaconvert.types.hls_interval_cadence


class HlsImageBasedTrickPlaySettings(TypedDict):
    interval_cadence: NotRequired[
        "aws_sdk_mediaconvert.types.hls_interval_cadence.HlsIntervalCadence"
    ]
    """The cadence MediaConvert follows for generating thumbnails. If set to FOLLOW_IFRAME, MediaConvert generates thumbnails for each IDR frame in the output (matching the GOP cadence). If set to FOLLOW_CUSTOM, MediaConvert generates thumbnails according to the interval you specify in thumbnailInterval. If set to FOLLOW_SEGMENTATION, MediaConvert generates thumbnail playlist entries that align exactly with video segment boundaries. FOLLOW_SEGMENTATION requires 1x1 tiling."""
    thumbnail_height: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min2_max4096.__integerMin2Max4096"
    ]
    """Height of each thumbnail within each tile image, in pixels. Leave blank to maintain aspect ratio with thumbnail width. If following the aspect ratio would lead to a total tile height greater than 4096, then the job will be rejected. Must be divisible by 2."""
    thumbnail_interval: NotRequired[
        "aws_sdk_mediaconvert.types.__double_min0_max2147483647.__doubleMin0Max2147483647"
    ]
    """Enter the interval, in seconds, that MediaConvert uses to generate thumbnails. If the interval you enter doesn't align with the output frame rate, MediaConvert automatically rounds the interval to align with the output frame rate. For example, if the output frame rate is 29.97 frames per second and you enter 5, MediaConvert uses a 150 frame interval to generate thumbnails."""
    thumbnail_width: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min8_max4096.__integerMin8Max4096"
    ]
    """Width of each thumbnail within each tile image, in pixels. Default is 312. Must be divisible by 8."""
    tile_height: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max2048.__integerMin1Max2048"
    ]
    """Number of thumbnails in each column of a tile image. Set a value between 1 and 2048."""
    tile_width: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max512.__integerMin1Max512"
    ]
    """Number of thumbnails in each row of a tile image. Set a value between 1 and 512."""


# --- restJson1 ser/de ---
def serialize_json(value: HlsImageBasedTrickPlaySettings) -> dict:
    out: dict = {}
    if "interval_cadence" in value:
        import aws_sdk_mediaconvert.types.hls_interval_cadence

        out["intervalCadence"] = (
            aws_sdk_mediaconvert.types.hls_interval_cadence.serialize_json(
                value["interval_cadence"]
            )
        )
    if "thumbnail_height" in value:
        out["thumbnailHeight"] = value["thumbnail_height"]
    if "thumbnail_interval" in value:
        out["thumbnailInterval"] = value["thumbnail_interval"]
    if "thumbnail_width" in value:
        out["thumbnailWidth"] = value["thumbnail_width"]
    if "tile_height" in value:
        out["tileHeight"] = value["tile_height"]
    if "tile_width" in value:
        out["tileWidth"] = value["tile_width"]
    return out


def deserialize_json(data: dict) -> HlsImageBasedTrickPlaySettings:
    out: HlsImageBasedTrickPlaySettings = {}  # type: ignore[typeddict-item]
    if "intervalCadence" in data:
        import aws_sdk_mediaconvert.types.hls_interval_cadence

        out["interval_cadence"] = (
            aws_sdk_mediaconvert.types.hls_interval_cadence.deserialize_json(
                data["intervalCadence"]
            )
        )
    if "thumbnailHeight" in data:
        out["thumbnail_height"] = data["thumbnailHeight"]
    if "thumbnailInterval" in data:
        out["thumbnail_interval"] = data["thumbnailInterval"]
    if "thumbnailWidth" in data:
        out["thumbnail_width"] = data["thumbnailWidth"]
    if "tileHeight" in data:
        out["tile_height"] = data["tileHeight"]
    if "tileWidth" in data:
        out["tile_width"] = data["tileWidth"]
    return out
