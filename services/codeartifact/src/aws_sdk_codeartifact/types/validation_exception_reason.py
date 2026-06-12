"""Generated from Smithy shape ``com.amazonaws.codeartifact#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeartifact.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "CANNOT_PARSE",
    "ENCRYPTION_KEY_ERROR",
    "FIELD_VALIDATION_FAILED",
    "UNKNOWN_OPERATION",
    "OTHER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CANNOT_PARSE",
        "ENCRYPTION_KEY_ERROR",
        "FIELD_VALIDATION_FAILED",
        "UNKNOWN_OPERATION",
        "OTHER",
    )
)


def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
