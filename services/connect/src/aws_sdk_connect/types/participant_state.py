"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ParticipantState: TypeAlias = Literal[
    "INITIAL",
    "CONNECTED",
    "DISCONNECTED",
    "MISSED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIAL",
        "CONNECTED",
        "DISCONNECTED",
        "MISSED",
    )
)


def serialize_json(value: ParticipantState) -> str:
    return value


def deserialize_json(data: str) -> ParticipantState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParticipantState value: {data!r}")
    return cast(ParticipantState, data)
