"""Generated from Smithy shape ``com.amazonaws.rbin#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rbin.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "INVALID_PAGE_TOKEN",
    "INVALID_PARAMETER_VALUE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVALID_PAGE_TOKEN",
        "INVALID_PARAMETER_VALUE",
    )
)


def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
