"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ReservationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

ReservationState: TypeAlias = Literal[
    "ACTIVE",
    "EXPIRED",
    "PROCESSING",
    "CANCELED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "EXPIRED",
        "PROCESSING",
        "CANCELED",
    )
)


def serialize_json(value: ReservationState) -> str:
    return value


def deserialize_json(data: str) -> ReservationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReservationState value: {data!r}")
    return cast(ReservationState, data)
