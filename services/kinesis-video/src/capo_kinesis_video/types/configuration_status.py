"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

ConfigurationStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationStatus:
    return cast(ConfigurationStatus, data)
