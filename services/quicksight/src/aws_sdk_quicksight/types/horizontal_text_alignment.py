"""Generated from Smithy shape ``com.amazonaws.quicksight#HorizontalTextAlignment``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

HorizontalTextAlignment: TypeAlias = Literal[
    "LEFT",
    "CENTER",
    "RIGHT",
    "AUTO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LEFT",
        "CENTER",
        "RIGHT",
        "AUTO",
    )
)


def serialize_json(value: HorizontalTextAlignment) -> str:
    return value


def deserialize_json(data: str) -> HorizontalTextAlignment:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HorizontalTextAlignment value: {data!r}")
    return cast(HorizontalTextAlignment, data)
