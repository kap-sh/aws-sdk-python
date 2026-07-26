"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ConflictExceptionType``."""

from typing import Literal, TypeAlias, cast

ConflictExceptionType: TypeAlias = Literal[
    "RESOURCE_IN_USE",
    "RESOURCE_ALREADY_EXISTS",
    "IDEMPOTENT_PARAMETER_MISMATCH",
    "CONFLICTING_OPERATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConflictExceptionType) -> str:
    return value


def deserialize_json(data: str) -> ConflictExceptionType:
    return cast(ConflictExceptionType, data)
