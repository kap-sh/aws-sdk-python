"""Generated from Smithy shape ``com.amazonaws.iot#SbomValidationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

SbomValidationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "SUCCEEDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "FAILED",
        "SUCCEEDED",
    )
)


def serialize_json(value: SbomValidationStatus) -> str:
    return value


def deserialize_json(data: str) -> SbomValidationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SbomValidationStatus value: {data!r}")
    return cast(SbomValidationStatus, data)
