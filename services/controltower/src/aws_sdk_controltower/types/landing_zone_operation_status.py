"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneOperationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_controltower.errors import DeserializationError

LandingZoneOperationStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "IN_PROGRESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "FAILED",
        "IN_PROGRESS",
    )
)


def serialize_json(value: LandingZoneOperationStatus) -> str:
    return value


def deserialize_json(data: str) -> LandingZoneOperationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LandingZoneOperationStatus value: {data!r}"
        )
    return cast(LandingZoneOperationStatus, data)
