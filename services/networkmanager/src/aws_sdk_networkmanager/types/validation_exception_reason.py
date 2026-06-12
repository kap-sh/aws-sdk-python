"""Generated from Smithy shape ``com.amazonaws.networkmanager#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "UnknownOperation",
    "CannotParse",
    "FieldValidationFailed",
    "Other",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UnknownOperation",
        "CannotParse",
        "FieldValidationFailed",
        "Other",
    )
)


def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
