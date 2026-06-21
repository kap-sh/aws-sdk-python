"""Generated from Smithy shape ``com.amazonaws.medialive#ReservationResolution``."""

from typing import Literal, TypeAlias, cast

"""Resolution based on lines of vertical resolution; SD is less than 720 lines, HD is 720 to 1080 lines, FHD is 1080 lines, UHD is greater than 1080 lines"""
ReservationResolution: TypeAlias = Literal[
    "SD",
    "HD",
    "FHD",
    "UHD",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservationResolution) -> str:
    return value


def deserialize_json(data: str) -> ReservationResolution:
    return cast(ReservationResolution, data)
