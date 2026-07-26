"""Generated from Smithy shape ``com.amazonaws.medialive#ReservationMaximumBitrate``."""

from typing import Literal, TypeAlias, cast

"""Maximum bitrate in megabits per second"""
ReservationMaximumBitrate: TypeAlias = Literal[
    "MAX_10_MBPS",
    "MAX_20_MBPS",
    "MAX_50_MBPS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservationMaximumBitrate) -> str:
    return value


def deserialize_json(data: str) -> ReservationMaximumBitrate:
    return cast(ReservationMaximumBitrate, data)
