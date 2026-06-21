"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantType``."""

from typing import Literal, TypeAlias, cast

ParticipantType: TypeAlias = Literal[
    "ALL",
    "MANAGER",
    "AGENT",
    "CUSTOMER",
    "THIRDPARTY",
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantType) -> str:
    return value


def deserialize_json(data: str) -> ParticipantType:
    return cast(ParticipantType, data)
