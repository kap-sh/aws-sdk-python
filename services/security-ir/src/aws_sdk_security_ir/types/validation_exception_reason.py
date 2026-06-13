"""Generated from Smithy shape ``com.amazonaws.securityir#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_security_ir.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "UNKNOWN_OPERATION",
    "CANNOT_PARSE",
    "FIELD_VALIDATION_FAILED",
    "OTHER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNKNOWN_OPERATION",
        "CANNOT_PARSE",
        "FIELD_VALIDATION_FAILED",
        "OTHER",
    )
)


def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
