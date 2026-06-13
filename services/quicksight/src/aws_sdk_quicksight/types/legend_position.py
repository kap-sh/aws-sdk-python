"""Generated from Smithy shape ``com.amazonaws.quicksight#LegendPosition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

LegendPosition: TypeAlias = Literal[
    "AUTO",
    "RIGHT",
    "BOTTOM",
    "TOP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "RIGHT",
        "BOTTOM",
        "TOP",
    )
)


def serialize_json(value: LegendPosition) -> str:
    return value


def deserialize_json(data: str) -> LegendPosition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LegendPosition value: {data!r}")
    return cast(LegendPosition, data)
