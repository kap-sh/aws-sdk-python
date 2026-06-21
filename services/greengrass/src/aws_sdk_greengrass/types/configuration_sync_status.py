"""Generated from Smithy shape ``com.amazonaws.greengrass#ConfigurationSyncStatus``."""

from typing import Literal, TypeAlias, cast

ConfigurationSyncStatus: TypeAlias = Literal[
    "InSync",
    "OutOfSync",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationSyncStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationSyncStatus:
    return cast(ConfigurationSyncStatus, data)
