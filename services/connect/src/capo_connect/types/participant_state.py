"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantState``."""

from typing import Literal, TypeAlias, cast

ParticipantState: TypeAlias = Literal[
    "INITIAL",
    "CONNECTED",
    "DISCONNECTED",
    "MISSED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantState) -> str:
    return value


def deserialize_json(data: str) -> ParticipantState:
    return cast(ParticipantState, data)
