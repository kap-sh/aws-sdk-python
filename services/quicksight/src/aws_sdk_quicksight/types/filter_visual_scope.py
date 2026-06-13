"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterVisualScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

FilterVisualScope: TypeAlias = Literal[
    "ALL_VISUALS",
    "SELECTED_VISUALS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_VISUALS",
        "SELECTED_VISUALS",
    )
)


def serialize_json(value: FilterVisualScope) -> str:
    return value


def deserialize_json(data: str) -> FilterVisualScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterVisualScope value: {data!r}")
    return cast(FilterVisualScope, data)
