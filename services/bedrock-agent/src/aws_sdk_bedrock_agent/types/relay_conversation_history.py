"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RelayConversationHistory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

RelayConversationHistory: TypeAlias = Literal[
    "TO_COLLABORATOR",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TO_COLLABORATOR",
        "DISABLED",
    )
)


def serialize_json(value: RelayConversationHistory) -> str:
    return value


def deserialize_json(data: str) -> RelayConversationHistory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RelayConversationHistory value: {data!r}")
    return cast(RelayConversationHistory, data)
