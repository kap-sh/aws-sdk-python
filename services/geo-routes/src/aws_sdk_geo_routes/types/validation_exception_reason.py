"""Generated from Smithy shape ``com.amazonaws.georoutes#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

ValidationExceptionReason: TypeAlias = Literal[
    "UnknownOperation",
    "Missing",
    "CannotParse",
    "FieldValidationFailed",
    "Other",
    "UnknownField",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
