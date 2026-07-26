"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#TargetedMessages``."""

from typing import Literal, TypeAlias, cast

TargetedMessages: TypeAlias = Literal[
    "ALL",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetedMessages) -> str:
    return value


def deserialize_json(data: str) -> TargetedMessages:
    return cast(TargetedMessages, data)
