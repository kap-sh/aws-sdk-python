"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RegistryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

RegistryStatus: TypeAlias = Literal[
    "CREATING",
    "READY",
    "UPDATING",
    "CREATE_FAILED",
    "UPDATE_FAILED",
    "DELETING",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "READY",
        "UPDATING",
        "CREATE_FAILED",
        "UPDATE_FAILED",
        "DELETING",
        "DELETE_FAILED",
    )
)


def serialize_json(value: RegistryStatus) -> str:
    return value


def deserialize_json(data: str) -> RegistryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RegistryStatus value: {data!r}")
    return cast(RegistryStatus, data)
