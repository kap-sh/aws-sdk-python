"""Generated from Smithy shape ``com.amazonaws.polly#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_polly.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "unsupportedOperation",
    "fieldValidationFailed",
    "other",
    "invalidInboundEvent",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "unsupportedOperation",
        "fieldValidationFailed",
        "other",
        "invalidInboundEvent",
    )
)


def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
