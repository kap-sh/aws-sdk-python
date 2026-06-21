"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#ConfigFileState``."""

from typing import Literal, TypeAlias, cast

ConfigFileState: TypeAlias = Literal[
    "Present",
    "Absent",
    "PresentWithErrors",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigFileState) -> str:
    return value


def deserialize_json(data: str) -> ConfigFileState:
    return cast(ConfigFileState, data)
