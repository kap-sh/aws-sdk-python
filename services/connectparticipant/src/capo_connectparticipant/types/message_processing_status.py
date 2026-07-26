"""Generated from Smithy shape ``com.amazonaws.connectparticipant#MessageProcessingStatus``."""

from typing import Literal, TypeAlias, cast

MessageProcessingStatus: TypeAlias = Literal[
    "PROCESSING",
    "FAILED",
    "REJECTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageProcessingStatus) -> str:
    return value


def deserialize_json(data: str) -> MessageProcessingStatus:
    return cast(MessageProcessingStatus, data)
