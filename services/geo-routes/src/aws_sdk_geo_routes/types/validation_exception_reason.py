"""Generated from Smithy shape ``com.amazonaws.georoutes#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "UnknownOperation",
    "Missing",
    "CannotParse",
    "FieldValidationFailed",
    "Other",
    "UnknownField",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UnknownOperation",
        "Missing",
        "CannotParse",
        "FieldValidationFailed",
        "Other",
        "UnknownField",
    )
)


def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
