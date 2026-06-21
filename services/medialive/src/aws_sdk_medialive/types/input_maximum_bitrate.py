"""Generated from Smithy shape ``com.amazonaws.medialive#InputMaximumBitrate``."""

from typing import Literal, TypeAlias, cast

"""Maximum input bitrate in megabits per second. Bitrates up to 50 Mbps are supported currently."""
InputMaximumBitrate: TypeAlias = Literal[
    "MAX_10_MBPS",
    "MAX_20_MBPS",
    "MAX_50_MBPS",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputMaximumBitrate) -> str:
    return value


def deserialize_json(data: str) -> InputMaximumBitrate:
    return cast(InputMaximumBitrate, data)
