"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#ParticipantRole``."""

from typing import Literal, TypeAlias, cast

ParticipantRole: TypeAlias = Literal[
    "AGENT",
    "CUSTOMER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantRole) -> str:
    return value


def deserialize_json(data: str) -> ParticipantRole:
    return cast(ParticipantRole, data)
