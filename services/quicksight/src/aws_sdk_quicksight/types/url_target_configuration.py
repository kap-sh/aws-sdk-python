"""Generated from Smithy shape ``com.amazonaws.quicksight#URLTargetConfiguration``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

URLTargetConfiguration: TypeAlias = Literal[
    "NEW_TAB",
    "NEW_WINDOW",
    "SAME_TAB",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NEW_TAB",
        "NEW_WINDOW",
        "SAME_TAB",
    )
)


def serialize_json(value: URLTargetConfiguration) -> str:
    return value


def deserialize_json(data: str) -> URLTargetConfiguration:
    if data not in _VALUES:
        raise DeserializationError(f"unknown URLTargetConfiguration value: {data!r}")
    return cast(URLTargetConfiguration, data)
