"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneDriftStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_controltower.errors import DeserializationError

LandingZoneDriftStatus: TypeAlias = Literal[
    "DRIFTED",
    "IN_SYNC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DRIFTED",
        "IN_SYNC",
    )
)


def serialize_json(value: LandingZoneDriftStatus) -> str:
    return value


def deserialize_json(data: str) -> LandingZoneDriftStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LandingZoneDriftStatus value: {data!r}")
    return cast(LandingZoneDriftStatus, data)
