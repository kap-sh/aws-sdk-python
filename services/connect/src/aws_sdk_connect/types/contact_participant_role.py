"""Generated from Smithy shape ``com.amazonaws.connect#ContactParticipantRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ContactParticipantRole: TypeAlias = Literal[
    "AGENT",
    "SYSTEM",
    "CUSTOM_BOT",
    "CUSTOMER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AGENT",
        "SYSTEM",
        "CUSTOM_BOT",
        "CUSTOMER",
    )
)


def serialize_json(value: ContactParticipantRole) -> str:
    return value


def deserialize_json(data: str) -> ContactParticipantRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactParticipantRole value: {data!r}")
    return cast(ContactParticipantRole, data)
