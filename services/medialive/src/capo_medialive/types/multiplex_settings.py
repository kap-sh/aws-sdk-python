"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0_max65535
    import capo_medialive.types.__integer_min0_max100000000
    import capo_medialive.types.__integer_min800_max3000
    import capo_medialive.types.__integer_min1000000_max100000000


class MultiplexSettings(TypedDict, closed=True):
    maximum_video_buffer_delay_milliseconds: NotRequired[
        "capo_medialive.types.__integer_min800_max3000.__integerMin800Max3000"
    ]
    """Maximum video buffer delay in milliseconds."""
    transport_stream_bitrate: NotRequired[
        "capo_medialive.types.__integer_min1000000_max100000000.__integerMin1000000Max100000000"
    ]
    """Transport stream bit rate."""
    transport_stream_id: NotRequired[
        "capo_medialive.types.__integer_min0_max65535.__integerMin0Max65535"
    ]
    """Transport stream ID."""
    transport_stream_reserved_bitrate: NotRequired[
        "capo_medialive.types.__integer_min0_max100000000.__integerMin0Max100000000"
    ]
    """Transport stream reserved bit rate."""


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexSettings) -> dict:
    out: dict = {}
    if "maximum_video_buffer_delay_milliseconds" in value:
        out["maximumVideoBufferDelayMilliseconds"] = value[
            "maximum_video_buffer_delay_milliseconds"
        ]
    if "transport_stream_bitrate" in value:
        out["transportStreamBitrate"] = value["transport_stream_bitrate"]
    if "transport_stream_id" in value:
        out["transportStreamId"] = value["transport_stream_id"]
    if "transport_stream_reserved_bitrate" in value:
        out["transportStreamReservedBitrate"] = value[
            "transport_stream_reserved_bitrate"
        ]
    return out


def deserialize_json(data: dict) -> MultiplexSettings:
    out: MultiplexSettings = {}  # type: ignore[typeddict-item]
    if "maximumVideoBufferDelayMilliseconds" in data:
        out["maximum_video_buffer_delay_milliseconds"] = data[
            "maximumVideoBufferDelayMilliseconds"
        ]
    if "transportStreamBitrate" in data:
        out["transport_stream_bitrate"] = data["transportStreamBitrate"]
    if "transportStreamId" in data:
        out["transport_stream_id"] = data["transportStreamId"]
    if "transportStreamReservedBitrate" in data:
        out["transport_stream_reserved_bitrate"] = data[
            "transportStreamReservedBitrate"
        ]
    return out
