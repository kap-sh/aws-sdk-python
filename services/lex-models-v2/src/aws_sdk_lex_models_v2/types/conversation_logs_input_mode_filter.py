"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationLogsInputModeFilter``."""

from typing import Literal, TypeAlias, cast

ConversationLogsInputModeFilter: TypeAlias = Literal[
    "Speech",
    "Text",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLogsInputModeFilter) -> str:
    return value


def deserialize_json(data: str) -> ConversationLogsInputModeFilter:
    return cast(ConversationLogsInputModeFilter, data)
