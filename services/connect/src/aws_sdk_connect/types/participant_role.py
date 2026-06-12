"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ParticipantRole: TypeAlias = Literal[
    "AGENT",
    "CUSTOMER",
    "SYSTEM",
    "CUSTOM_BOT",
    "SUPERVISOR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AGENT",
        "CUSTOMER",
        "SYSTEM",
        "CUSTOM_BOT",
        "SUPERVISOR",
    )
)


def serialize_json(value: ParticipantRole) -> str:
    return value


def deserialize_json(data: str) -> ParticipantRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParticipantRole value: {data!r}")
    return cast(ParticipantRole, data)
