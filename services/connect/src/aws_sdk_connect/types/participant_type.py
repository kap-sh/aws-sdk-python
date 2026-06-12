"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ParticipantType: TypeAlias = Literal[
    "ALL",
    "MANAGER",
    "AGENT",
    "CUSTOMER",
    "THIRDPARTY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "MANAGER",
        "AGENT",
        "CUSTOMER",
        "THIRDPARTY",
    )
)


def serialize_json(value: ParticipantType) -> str:
    return value


def deserialize_json(data: str) -> ParticipantType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParticipantType value: {data!r}")
    return cast(ParticipantType, data)
