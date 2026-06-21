"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#ConversationMode``."""

from typing import Literal, TypeAlias, cast

ConversationMode: TypeAlias = Literal[
    "AUDIO",
    "TEXT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConversationMode) -> str:
    return value


def deserialize_json(data: str) -> ConversationMode:
    return cast(ConversationMode, data)
