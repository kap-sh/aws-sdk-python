"""Generated from Smithy shape ``com.amazonaws.quicksight#TooltipTitleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TooltipTitleType: TypeAlias = Literal[
    "NONE",
    "PRIMARY_VALUE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "PRIMARY_VALUE",
    )
)


def serialize_json(value: TooltipTitleType) -> str:
    return value


def deserialize_json(data: str) -> TooltipTitleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TooltipTitleType value: {data!r}")
    return cast(TooltipTitleType, data)
