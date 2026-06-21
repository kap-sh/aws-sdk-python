"""Generated from Smithy shape ``com.amazonaws.repostspace#ConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

ConfigurationStatus: TypeAlias = Literal[
    "CONFIGURED",
    "UNCONFIGURED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationStatus:
    return cast(ConfigurationStatus, data)
