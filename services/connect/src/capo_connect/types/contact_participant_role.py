"""Generated from Smithy shape ``com.amazonaws.connect#ContactParticipantRole``."""

from typing import Literal, TypeAlias, cast

ContactParticipantRole: TypeAlias = Literal[
    "AGENT",
    "SYSTEM",
    "CUSTOM_BOT",
    "CUSTOMER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactParticipantRole) -> str:
    return value


def deserialize_json(data: str) -> ContactParticipantRole:
    return cast(ContactParticipantRole, data)
