"""Generated from Smithy shape ``com.amazonaws.quicksight#SelectedTooltipType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SelectedTooltipType: TypeAlias = Literal[
    "BASIC",
    "DETAILED",
    "SHEET",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASIC",
        "DETAILED",
        "SHEET",
    )
)


def serialize_json(value: SelectedTooltipType) -> str:
    return value


def deserialize_json(data: str) -> SelectedTooltipType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SelectedTooltipType value: {data!r}")
    return cast(SelectedTooltipType, data)
