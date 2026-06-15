"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConfigurationBundleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "CREATING",
        "CREATE_FAILED",
        "UPDATING",
        "UPDATE_FAILED",
        "DELETING",
        "DELETE_FAILED",
    )
)


def serialize_json(value: ConfigurationBundleStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationBundleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigurationBundleStatus value: {data!r}")
    return cast(ConfigurationBundleStatus, data)
