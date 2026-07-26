"""Generated from Smithy shape ``com.amazonaws.codeartifact#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

ValidationExceptionReason: TypeAlias = Literal[
    "CANNOT_PARSE",
    "ENCRYPTION_KEY_ERROR",
    "FIELD_VALIDATION_FAILED",
    "UNKNOWN_OPERATION",
    "OTHER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
