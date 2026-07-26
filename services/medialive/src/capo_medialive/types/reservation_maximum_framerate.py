"""Generated from Smithy shape ``com.amazonaws.medialive#ReservationMaximumFramerate``."""

from typing import Literal, TypeAlias, cast

"""Maximum framerate in frames per second (Outputs only)"""
ReservationMaximumFramerate: TypeAlias = Literal[
    "MAX_30_FPS",
    "MAX_60_FPS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservationMaximumFramerate) -> str:
    return value


def deserialize_json(data: str) -> ReservationMaximumFramerate:
    return cast(ReservationMaximumFramerate, data)
