"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatMode``."""

from typing import Literal, TypeAlias, cast

ChatMode: TypeAlias = Literal[
    "RETRIEVAL_MODE",
    "CREATOR_MODE",
    "PLUGIN_MODE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChatMode) -> str:
    return value


def deserialize_json(data: str) -> ChatMode:
    return cast(ChatMode, data)
