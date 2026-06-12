"""Generated from Smithy shape ``com.amazonaws.chime#MemberType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime.errors import DeserializationError

MemberType: TypeAlias = Literal[
    "User",
    "Bot",
    "Webhook",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "User",
        "Bot",
        "Webhook",
    )
)


def serialize_json(value: MemberType) -> str:
    return value


def deserialize_json(data: str) -> MemberType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MemberType value: {data!r}")
    return cast(MemberType, data)
