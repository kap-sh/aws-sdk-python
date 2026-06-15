"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

PolicyStatus: TypeAlias = Literal[
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


def serialize_json(value: PolicyStatus) -> str:
    return value


def deserialize_json(data: str) -> PolicyStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PolicyStatus value: {data!r}")
    return cast(PolicyStatus, data)
