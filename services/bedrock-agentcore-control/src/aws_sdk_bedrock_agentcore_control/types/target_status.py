"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TargetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

TargetStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "UPDATE_UNSUCCESSFUL",
    "DELETING",
    "READY",
    "FAILED",
    "SYNCHRONIZING",
    "SYNCHRONIZE_UNSUCCESSFUL",
    "CREATE_PENDING_AUTH",
    "UPDATE_PENDING_AUTH",
    "SYNCHRONIZE_PENDING_AUTH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "UPDATE_UNSUCCESSFUL",
        "DELETING",
        "READY",
        "FAILED",
        "SYNCHRONIZING",
        "SYNCHRONIZE_UNSUCCESSFUL",
        "CREATE_PENDING_AUTH",
        "UPDATE_PENDING_AUTH",
        "SYNCHRONIZE_PENDING_AUTH",
    )
)


def serialize_json(value: TargetStatus) -> str:
    return value


def deserialize_json(data: str) -> TargetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetStatus value: {data!r}")
    return cast(TargetStatus, data)
