"""Generated from Smithy shape ``com.amazonaws.ivschat#ChatTokenCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivschat.types.chat_token_capability

ChatTokenCapabilities: TypeAlias = list[
    "capo_ivschat.types.chat_token_capability.ChatTokenCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChatTokenCapabilities) -> list:
    return list(value)


def deserialize_json(data: list) -> ChatTokenCapabilities:
    return list(data)
