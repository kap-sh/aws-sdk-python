"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RelayConversationHistory``."""

from typing import Literal, TypeAlias, cast

RelayConversationHistory: TypeAlias = Literal[
    "TO_COLLABORATOR",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RelayConversationHistory) -> str:
    return value


def deserialize_json(data: str) -> RelayConversationHistory:
    return cast(RelayConversationHistory, data)
