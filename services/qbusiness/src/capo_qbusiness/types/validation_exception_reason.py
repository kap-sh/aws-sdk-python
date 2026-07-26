"""Generated from Smithy shape ``com.amazonaws.qbusiness#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

ValidationExceptionReason: TypeAlias = Literal[
    "CANNOT_PARSE",
    "FIELD_VALIDATION_FAILED",
    "UNKNOWN_OPERATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
