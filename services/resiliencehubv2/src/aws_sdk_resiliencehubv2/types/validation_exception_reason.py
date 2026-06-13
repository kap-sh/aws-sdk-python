"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "INVALID_FIELD_VALUE",
    "DUPLICATE_VALUE",
    "MISSING_REQUIRED_FIELD",
    "OTHER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVALID_FIELD_VALUE",
        "DUPLICATE_VALUE",
        "MISSING_REQUIRED_FIELD",
        "OTHER",
    )
)


def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
