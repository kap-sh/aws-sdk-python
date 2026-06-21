"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConfigurationBundleStatus``."""

from typing import Literal, TypeAlias, cast

ConfigurationBundleStatus: TypeAlias = Literal[
    "ACTIVE",
    "CREATING",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "DELETING",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationBundleStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationBundleStatus:
    return cast(ConfigurationBundleStatus, data)
