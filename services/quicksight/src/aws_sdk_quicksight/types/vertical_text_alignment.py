"""Generated from Smithy shape ``com.amazonaws.quicksight#VerticalTextAlignment``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

VerticalTextAlignment: TypeAlias = Literal[
    "TOP",
    "MIDDLE",
    "BOTTOM",
    "AUTO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TOP",
        "MIDDLE",
        "BOTTOM",
        "AUTO",
    )
)


def serialize_json(value: VerticalTextAlignment) -> str:
    return value


def deserialize_json(data: str) -> VerticalTextAlignment:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VerticalTextAlignment value: {data!r}")
    return cast(VerticalTextAlignment, data)
