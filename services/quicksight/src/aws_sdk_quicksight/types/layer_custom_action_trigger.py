"""Generated from Smithy shape ``com.amazonaws.quicksight#LayerCustomActionTrigger``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

LayerCustomActionTrigger: TypeAlias = Literal[
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


def serialize_json(value: LayerCustomActionTrigger) -> str:
    return value


def deserialize_json(data: str) -> LayerCustomActionTrigger:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LayerCustomActionTrigger value: {data!r}")
    return cast(LayerCustomActionTrigger, data)
