"""Generated from Smithy shape ``com.amazonaws.qbusiness#SystemMessageType``."""

from typing import Literal, TypeAlias, cast

SystemMessageType: TypeAlias = Literal[
    "RESPONSE",
    "GROUNDED_RESPONSE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SystemMessageType) -> str:
    return value


def deserialize_json(data: str) -> SystemMessageType:
    return cast(SystemMessageType, data)
