"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ConflictExceptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

ConflictExceptionType: TypeAlias = Literal[
    "RESOURCE_IN_USE",
    "RESOURCE_ALREADY_EXISTS",
    "IDEMPOTENT_PARAMETER_MISMATCH",
    "CONFLICTING_OPERATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESOURCE_IN_USE",
        "RESOURCE_ALREADY_EXISTS",
        "IDEMPOTENT_PARAMETER_MISMATCH",
        "CONFLICTING_OPERATION",
    )
)


def serialize_json(value: ConflictExceptionType) -> str:
    return value


def deserialize_json(data: str) -> ConflictExceptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConflictExceptionType value: {data!r}")
    return cast(ConflictExceptionType, data)
