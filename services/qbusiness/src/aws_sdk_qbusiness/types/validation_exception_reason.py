"""Generated from Smithy shape ``com.amazonaws.qbusiness#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "CANNOT_PARSE",
    "FIELD_VALIDATION_FAILED",
    "UNKNOWN_OPERATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CANNOT_PARSE",
        "FIELD_VALIDATION_FAILED",
        "UNKNOWN_OPERATION",
    )
)


def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
