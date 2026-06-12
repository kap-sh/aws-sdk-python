"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ConversationRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

ConversationRole: TypeAlias = Literal[
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


def serialize_json(value: ConversationRole) -> str:
    return value


def deserialize_json(data: str) -> ConversationRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConversationRole value: {data!r}")
    return cast(ConversationRole, data)
