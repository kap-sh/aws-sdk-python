"""Generated from Smithy shape ``com.amazonaws.qbusiness#PluginBuildStatus``."""

from typing import Literal, TypeAlias, cast

PluginBuildStatus: TypeAlias = Literal[
    "READY",
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PluginBuildStatus) -> str:
    return value


def deserialize_json(data: str) -> PluginBuildStatus:
    return cast(PluginBuildStatus, data)
