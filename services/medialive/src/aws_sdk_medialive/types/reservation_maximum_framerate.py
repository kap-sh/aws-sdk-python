"""Generated from Smithy shape ``com.amazonaws.medialive#ReservationMaximumFramerate``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Maximum framerate in frames per second (Outputs only)"""
ReservationMaximumFramerate: TypeAlias = Literal[
    "MAX_30_FPS",
    "MAX_60_FPS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MAX_30_FPS",
        "MAX_60_FPS",
    )
)


def serialize_json(value: ReservationMaximumFramerate) -> str:
    return value


def deserialize_json(data: str) -> ReservationMaximumFramerate:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ReservationMaximumFramerate value: {data!r}"
        )
    return cast(ReservationMaximumFramerate, data)
