"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

BrowserStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "READY",
    "DELETING",
    "DELETE_FAILED",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATE_FAILED",
        "READY",
        "DELETING",
        "DELETE_FAILED",
        "DELETED",
    )
)


def serialize_json(value: BrowserStatus) -> str:
    return value


def deserialize_json(data: str) -> BrowserStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BrowserStatus value: {data!r}")
    return cast(BrowserStatus, data)
