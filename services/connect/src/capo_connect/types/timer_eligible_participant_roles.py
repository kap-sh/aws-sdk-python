"""Generated from Smithy shape ``com.amazonaws.connect#TimerEligibleParticipantRoles``."""

from typing import Literal, TypeAlias, cast

TimerEligibleParticipantRoles: TypeAlias = Literal[
    "CUSTOMER",
    "AGENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: TimerEligibleParticipantRoles) -> str:
    return value


def deserialize_json(data: str) -> TimerEligibleParticipantRoles:
    return cast(TimerEligibleParticipantRoles, data)
