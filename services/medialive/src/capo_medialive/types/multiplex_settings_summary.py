"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexSettingsSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min1000000_max100000000


class MultiplexSettingsSummary(TypedDict, closed=True):
    transport_stream_bitrate: NotRequired[
        "capo_medialive.types.__integer_min1000000_max100000000.__integerMin1000000Max100000000"
    ]
    """Transport stream bit rate."""


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexSettingsSummary) -> dict:
    out: dict = {}
    if "transport_stream_bitrate" in value:
        out["transportStreamBitrate"] = value["transport_stream_bitrate"]
    return out


def deserialize_json(data: dict) -> MultiplexSettingsSummary:
    out: MultiplexSettingsSummary = {}  # type: ignore[typeddict-item]
    if "transportStreamBitrate" in data:
        out["transport_stream_bitrate"] = data["transportStreamBitrate"]
    return out
