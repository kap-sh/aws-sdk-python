"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

Status: TypeAlias = Literal[
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


def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
