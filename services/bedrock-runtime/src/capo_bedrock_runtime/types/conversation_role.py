"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ConversationRole``."""

from typing import Literal, TypeAlias, cast

ConversationRole: TypeAlias = Literal[
    "user",
    "assistant",
    "system",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConversationRole) -> str:
    return value


def deserialize_json(data: str) -> ConversationRole:
    return cast(ConversationRole, data)
