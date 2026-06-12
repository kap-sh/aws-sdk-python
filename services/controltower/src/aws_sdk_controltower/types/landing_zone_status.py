"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_controltower.errors import DeserializationError

LandingZoneStatus: TypeAlias = Literal[
    "ACTIVE",
    "PROCESSING",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "PROCESSING",
        "FAILED",
    )
)


def serialize_json(value: LandingZoneStatus) -> str:
    return value


def deserialize_json(data: str) -> LandingZoneStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LandingZoneStatus value: {data!r}")
    return cast(LandingZoneStatus, data)
