"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationEndState``."""

from typing import Literal, TypeAlias, cast

ConversationEndState: TypeAlias = Literal[
    "Success",
    "Failure",
    "Dropped",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConversationEndState) -> str:
    return value


def deserialize_json(data: str) -> ConversationEndState:
    return cast(ConversationEndState, data)
