"""Generated from Smithy shape ``com.amazonaws.repostspace#ChannelRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_repostspace.errors import DeserializationError

ChannelRole: TypeAlias = Literal[
    "ASKER",
    "EXPERT",
    "MODERATOR",
    "SUPPORTREQUESTOR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASKER",
        "EXPERT",
        "MODERATOR",
        "SUPPORTREQUESTOR",
    )
)


def serialize_json(value: ChannelRole) -> str:
    return value


def deserialize_json(data: str) -> ChannelRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChannelRole value: {data!r}")
    return cast(ChannelRole, data)
