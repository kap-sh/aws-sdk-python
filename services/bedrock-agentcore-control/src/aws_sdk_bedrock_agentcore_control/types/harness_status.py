"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

HarnessStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "READY",
    "DELETING",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATE_FAILED",
        "UPDATING",
        "UPDATE_FAILED",
        "READY",
        "DELETING",
        "DELETE_FAILED",
    )
)


def serialize_json(value: HarnessStatus) -> str:
    return value


def deserialize_json(data: str) -> HarnessStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HarnessStatus value: {data!r}")
    return cast(HarnessStatus, data)
