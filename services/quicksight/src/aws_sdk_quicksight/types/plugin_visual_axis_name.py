"""Generated from Smithy shape ``com.amazonaws.quicksight#PluginVisualAxisName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

PluginVisualAxisName: TypeAlias = Literal[
    "GROUP_BY",
    "VALUE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GROUP_BY",
        "VALUE",
    )
)


def serialize_json(value: PluginVisualAxisName) -> str:
    return value


def deserialize_json(data: str) -> PluginVisualAxisName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PluginVisualAxisName value: {data!r}")
    return cast(PluginVisualAxisName, data)
