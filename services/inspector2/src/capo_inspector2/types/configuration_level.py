"""Generated from Smithy shape ``com.amazonaws.inspector2#ConfigurationLevel``."""

from typing import Literal, TypeAlias, cast

ConfigurationLevel: TypeAlias = Literal[
    "ORGANIZATION",
    "ACCOUNT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationLevel) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationLevel:
    return cast(ConfigurationLevel, data)
