"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneOperationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_controltower.errors import DeserializationError

LandingZoneOperationType: TypeAlias = Literal[
    "DELETE",
    "CREATE",
    "UPDATE",
    "RESET",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DELETE",
        "CREATE",
        "UPDATE",
        "RESET",
    )
)


def serialize_json(value: LandingZoneOperationType) -> str:
    return value


def deserialize_json(data: str) -> LandingZoneOperationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LandingZoneOperationType value: {data!r}")
    return cast(LandingZoneOperationType, data)
