"""Generated from Smithy shape ``com.amazonaws.connect#PropertyValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

PropertyValidationExceptionReason: TypeAlias = Literal[
    "INVALID_FORMAT",
    "UNIQUE_CONSTRAINT_VIOLATED",
    "REFERENCED_RESOURCE_NOT_FOUND",
    "RESOURCE_NAME_ALREADY_EXISTS",
    "REQUIRED_PROPERTY_MISSING",
    "NOT_SUPPORTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PropertyValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> PropertyValidationExceptionReason:
    return cast(PropertyValidationExceptionReason, data)
