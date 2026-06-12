"""Generated from Smithy shape ``com.amazonaws.connect#TimerEligibleParticipantRoles``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

TimerEligibleParticipantRoles: TypeAlias = Literal[
    "CUSTOMER",
    "AGENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOMER",
        "AGENT",
    )
)


def serialize_json(value: TimerEligibleParticipantRoles) -> str:
    return value


def deserialize_json(data: str) -> TimerEligibleParticipantRoles:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TimerEligibleParticipantRoles value: {data!r}"
        )
    return cast(TimerEligibleParticipantRoles, data)
