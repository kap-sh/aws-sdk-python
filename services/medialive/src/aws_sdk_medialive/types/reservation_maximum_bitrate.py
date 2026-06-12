"""Generated from Smithy shape ``com.amazonaws.medialive#ReservationMaximumBitrate``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Maximum bitrate in megabits per second"""
ReservationMaximumBitrate: TypeAlias = Literal[
    "MAX_10_MBPS",
    "MAX_20_MBPS",
    "MAX_50_MBPS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MAX_10_MBPS",
        "MAX_20_MBPS",
        "MAX_50_MBPS",
    )
)


def serialize_json(value: ReservationMaximumBitrate) -> str:
    return value


def deserialize_json(data: str) -> ReservationMaximumBitrate:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReservationMaximumBitrate value: {data!r}")
    return cast(ReservationMaximumBitrate, data)
