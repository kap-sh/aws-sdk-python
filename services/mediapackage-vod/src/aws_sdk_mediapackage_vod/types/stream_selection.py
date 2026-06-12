"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#StreamSelection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__integer
    import aws_sdk_mediapackage_vod.types.stream_order


class StreamSelection(TypedDict):
    max_video_bits_per_second: NotRequired[
        "aws_sdk_mediapackage_vod.types.__integer.__integer"
    ]
    """The maximum video bitrate (bps) to include in output."""
    min_video_bits_per_second: NotRequired[
        "aws_sdk_mediapackage_vod.types.__integer.__integer"
    ]
    """The minimum video bitrate (bps) to include in output."""
    stream_order: NotRequired["aws_sdk_mediapackage_vod.types.stream_order.StreamOrder"]
    """A directive that determines the order of streams in the output."""


# --- restJson1 ser/de ---
def serialize_json(value: StreamSelection) -> dict:
    out: dict = {}
    if "max_video_bits_per_second" in value:
        out["maxVideoBitsPerSecond"] = value["max_video_bits_per_second"]
    if "min_video_bits_per_second" in value:
        out["minVideoBitsPerSecond"] = value["min_video_bits_per_second"]
    if "stream_order" in value:
        import aws_sdk_mediapackage_vod.types.stream_order

        out["streamOrder"] = aws_sdk_mediapackage_vod.types.stream_order.serialize_json(
            value["stream_order"]
        )
    return out


def deserialize_json(data: dict) -> StreamSelection:
    out: StreamSelection = {}  # type: ignore[typeddict-item]
    if "maxVideoBitsPerSecond" in data:
        out["max_video_bits_per_second"] = data["maxVideoBitsPerSecond"]
    if "minVideoBitsPerSecond" in data:
        out["min_video_bits_per_second"] = data["minVideoBitsPerSecond"]
    if "streamOrder" in data:
        import aws_sdk_mediapackage_vod.types.stream_order

        out["stream_order"] = (
            aws_sdk_mediapackage_vod.types.stream_order.deserialize_json(
                data["streamOrder"]
            )
        )
    return out
