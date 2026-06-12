"""Generated from Smithy shape ``com.amazonaws.medialive#ReservationResolution``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Resolution based on lines of vertical resolution; SD is less than 720 lines, HD is 720 to 1080 lines, FHD is 1080 lines, UHD is greater than 1080 lines"""
ReservationResolution: TypeAlias = Literal[
    "SD",
    "HD",
    "FHD",
    "UHD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SD",
        "HD",
        "FHD",
        "UHD",
    )
)


def serialize_json(value: ReservationResolution) -> str:
    return value


def deserialize_json(data: str) -> ReservationResolution:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReservationResolution value: {data!r}")
    return cast(ReservationResolution, data)
