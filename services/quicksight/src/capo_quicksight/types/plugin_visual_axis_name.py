"""Generated from Smithy shape ``com.amazonaws.quicksight#PluginVisualAxisName``."""

from typing import Literal, TypeAlias, cast

PluginVisualAxisName: TypeAlias = Literal[
    "GROUP_BY",
    "VALUE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PluginVisualAxisName) -> str:
    return value


def deserialize_json(data: str) -> PluginVisualAxisName:
    return cast(PluginVisualAxisName, data)
