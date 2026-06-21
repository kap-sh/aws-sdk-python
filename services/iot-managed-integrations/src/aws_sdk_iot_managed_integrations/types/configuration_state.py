"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ConfigurationState``."""

from typing import Literal, TypeAlias, cast

ConfigurationState: TypeAlias = Literal[
    "ENABLED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationState) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationState:
    return cast(ConfigurationState, data)
