"""Generated from Smithy shape ``com.amazonaws.iot#SbomValidationResult``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

SbomValidationResult: TypeAlias = Literal[
    "FAILED",
    "SUCCEEDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "SUCCEEDED",
    )
)


def serialize_json(value: SbomValidationResult) -> str:
    return value


def deserialize_json(data: str) -> SbomValidationResult:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SbomValidationResult value: {data!r}")
    return cast(SbomValidationResult, data)
