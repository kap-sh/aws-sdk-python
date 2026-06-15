"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessConversationRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

HarnessConversationRole: TypeAlias = Literal[
    "user",
    "assistant",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "user",
        "assistant",
    )
)


def serialize_json(value: HarnessConversationRole) -> str:
    return value


def deserialize_json(data: str) -> HarnessConversationRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HarnessConversationRole value: {data!r}")
    return cast(HarnessConversationRole, data)
