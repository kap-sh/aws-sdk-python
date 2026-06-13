"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualCustomActionTrigger``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

VisualCustomActionTrigger: TypeAlias = Literal[
    "DATA_POINT_CLICK",
    "DATA_POINT_MENU",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DATA_POINT_CLICK",
        "DATA_POINT_MENU",
    )
)


def serialize_json(value: VisualCustomActionTrigger) -> str:
    return value


def deserialize_json(data: str) -> VisualCustomActionTrigger:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VisualCustomActionTrigger value: {data!r}")
    return cast(VisualCustomActionTrigger, data)
