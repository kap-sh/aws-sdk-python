"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

ValidationExceptionReason: TypeAlias = Literal[
    "INVALID_FIELD_VALUE",
    "DUPLICATE_VALUE",
    "MISSING_REQUIRED_FIELD",
    "OTHER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
