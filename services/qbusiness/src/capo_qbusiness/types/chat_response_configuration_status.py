"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatResponseConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

ChatResponseConfigurationStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "FAILED",
    "ACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChatResponseConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> ChatResponseConfigurationStatus:
    return cast(ChatResponseConfigurationStatus, data)
