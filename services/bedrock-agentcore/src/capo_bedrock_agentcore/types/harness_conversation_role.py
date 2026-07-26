"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessConversationRole``."""

from typing import Literal, TypeAlias, cast

HarnessConversationRole: TypeAlias = Literal[
    "user",
    "assistant",
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessConversationRole) -> str:
    return value


def deserialize_json(data: str) -> HarnessConversationRole:
    return cast(HarnessConversationRole, data)
