"""Generated from Smithy shape ``com.amazonaws.devopsguru#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

ValidationExceptionReason: TypeAlias = Literal[
    "UNKNOWN_OPERATION",
    "CANNOT_PARSE",
    "FIELD_VALIDATION_FAILED",
    "OTHER",
    "INVALID_PARAMETER_COMBINATION",
    "PARAMETER_INCONSISTENT_WITH_SERVICE_STATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
