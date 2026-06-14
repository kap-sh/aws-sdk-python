"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyEngineStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

PolicyEngineStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "CREATE_FAILED",
    "UPDATE_FAILED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "DELETING",
        "CREATE_FAILED",
        "UPDATE_FAILED",
        "DELETE_FAILED",
    )
)


def serialize_json(value: PolicyEngineStatus) -> str:
    return value


def deserialize_json(data: str) -> PolicyEngineStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PolicyEngineStatus value: {data!r}")
    return cast(PolicyEngineStatus, data)
