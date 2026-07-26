"""Generated from Smithy shape ``com.amazonaws.iot#ConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

ConfigurationStatus: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationStatus:
    return cast(ConfigurationStatus, data)
