"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ConfigurationState``."""

from typing import Literal, TypeAlias, cast

ConfigurationState: TypeAlias = Literal[
    "ACTIVE",
    "UPDATE_IN_PROGRESS",
    "UPDATE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationState) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationState:
    return cast(ConfigurationState, data)
