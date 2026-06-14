"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ABTestStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

ABTestStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "DELETING",
    "DELETE_FAILED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "CREATE_FAILED",
        "UPDATING",
        "UPDATE_FAILED",
        "DELETING",
        "DELETE_FAILED",
        "FAILED",
    )
)


def serialize_json(value: ABTestStatus) -> str:
    return value


def deserialize_json(data: str) -> ABTestStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ABTestStatus value: {data!r}")
    return cast(ABTestStatus, data)
