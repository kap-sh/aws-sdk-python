"""Generated from Smithy shape ``com.amazonaws.quicksight#TemplateErrorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TemplateErrorType: TypeAlias = Literal[
    "SOURCE_NOT_FOUND",
    "DATA_SET_NOT_FOUND",
    "INTERNAL_FAILURE",
    "ACCESS_DENIED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SOURCE_NOT_FOUND",
        "DATA_SET_NOT_FOUND",
        "INTERNAL_FAILURE",
        "ACCESS_DENIED",
    )
)


def serialize_json(value: TemplateErrorType) -> str:
    return value


def deserialize_json(data: str) -> TemplateErrorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TemplateErrorType value: {data!r}")
    return cast(TemplateErrorType, data)
