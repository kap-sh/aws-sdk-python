"""Generated from Smithy shape ``com.amazonaws.connect#PropertyValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

PropertyValidationExceptionReason: TypeAlias = Literal[
    "INVALID_FORMAT",
    "UNIQUE_CONSTRAINT_VIOLATED",
    "REFERENCED_RESOURCE_NOT_FOUND",
    "RESOURCE_NAME_ALREADY_EXISTS",
    "REQUIRED_PROPERTY_MISSING",
    "NOT_SUPPORTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVALID_FORMAT",
        "UNIQUE_CONSTRAINT_VIOLATED",
        "REFERENCED_RESOURCE_NOT_FOUND",
        "RESOURCE_NAME_ALREADY_EXISTS",
        "REQUIRED_PROPERTY_MISSING",
        "NOT_SUPPORTED",
    )
)


def serialize_json(value: PropertyValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> PropertyValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PropertyValidationExceptionReason value: {data!r}"
        )
    return cast(PropertyValidationExceptionReason, data)
