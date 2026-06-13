"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualHighlightTrigger``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

VisualHighlightTrigger: TypeAlias = Literal[
    "DATA_POINT_CLICK",
    "DATA_POINT_HOVER",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DATA_POINT_CLICK",
        "DATA_POINT_HOVER",
        "NONE",
    )
)


def serialize_json(value: VisualHighlightTrigger) -> str:
    return value


def deserialize_json(data: str) -> VisualHighlightTrigger:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VisualHighlightTrigger value: {data!r}")
    return cast(VisualHighlightTrigger, data)
