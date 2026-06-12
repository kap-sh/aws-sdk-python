"""Generated from Smithy shape ``com.amazonaws.iot#SbomValidationErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

SbomValidationErrorCode: TypeAlias = Literal[
    "INCOMPATIBLE_FORMAT",
    "FILE_SIZE_LIMIT_EXCEEDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCOMPATIBLE_FORMAT",
        "FILE_SIZE_LIMIT_EXCEEDED",
    )
)


def serialize_json(value: SbomValidationErrorCode) -> str:
    return value


def deserialize_json(data: str) -> SbomValidationErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SbomValidationErrorCode value: {data!r}")
    return cast(SbomValidationErrorCode, data)
