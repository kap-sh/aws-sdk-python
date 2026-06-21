"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantTimerAction``."""

from typing import Literal, TypeAlias, cast

ParticipantTimerAction: TypeAlias = Literal["Unset",]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantTimerAction) -> str:
    return value


def deserialize_json(data: str) -> ParticipantTimerAction:
    return cast(ParticipantTimerAction, data)
