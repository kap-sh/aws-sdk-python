"""Generated from Smithy shape ``com.amazonaws.quicksight#TooltipTarget``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TooltipTarget: TypeAlias = Literal[
    "BOTH",
    "BAR",
    "LINE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BOTH",
        "BAR",
        "LINE",
    )
)


def serialize_json(value: TooltipTarget) -> str:
    return value


def deserialize_json(data: str) -> TooltipTarget:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TooltipTarget value: {data!r}")
    return cast(TooltipTarget, data)
