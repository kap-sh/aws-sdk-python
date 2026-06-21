"""Generated from Smithy shape ``com.amazonaws.kafka#ConfigurationState``."""

from typing import Literal, TypeAlias, cast

"""<p>The state of a configuration.</p>"""
ConfigurationState: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationState) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationState:
    return cast(ConfigurationState, data)
