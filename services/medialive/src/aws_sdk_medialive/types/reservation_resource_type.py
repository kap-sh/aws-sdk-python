"""Generated from Smithy shape ``com.amazonaws.medialive#ReservationResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Resource type, 'INPUT', 'OUTPUT', 'MULTIPLEX', or 'CHANNEL'"""
ReservationResourceType: TypeAlias = Literal[
    "INPUT",
    "OUTPUT",
    "MULTIPLEX",
    "CHANNEL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INPUT",
        "OUTPUT",
        "MULTIPLEX",
        "CHANNEL",
    )
)


def serialize_json(value: ReservationResourceType) -> str:
    return value


def deserialize_json(data: str) -> ReservationResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReservationResourceType value: {data!r}")
    return cast(ReservationResourceType, data)
