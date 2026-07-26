"""Generated from Smithy shape ``com.amazonaws.qbusiness#PluginState``."""

from typing import Literal, TypeAlias, cast

PluginState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PluginState) -> str:
    return value


def deserialize_json(data: str) -> PluginState:
    return cast(PluginState, data)
