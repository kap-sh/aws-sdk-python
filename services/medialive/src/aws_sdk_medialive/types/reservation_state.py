"""Generated from Smithy shape ``com.amazonaws.medialive#ReservationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Current reservation state"""
ReservationState: TypeAlias = Literal[
    "ACTIVE",
    "EXPIRED",
    "CANCELED",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "EXPIRED",
        "CANCELED",
        "DELETED",
    )
)


def serialize_json(value: ReservationState) -> str:
    return value


def deserialize_json(data: str) -> ReservationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReservationState value: {data!r}")
    return cast(ReservationState, data)
