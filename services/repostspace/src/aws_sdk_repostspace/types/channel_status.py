"""Generated from Smithy shape ``com.amazonaws.repostspace#ChannelStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_repostspace.errors import DeserializationError

ChannelStatus: TypeAlias = Literal[
    "CREATED",
    "CREATING",
    "CREATE_FAILED",
    "DELETED",
    "DELETING",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "CREATING",
        "CREATE_FAILED",
        "DELETED",
        "DELETING",
        "DELETE_FAILED",
    )
)


def serialize_json(value: ChannelStatus) -> str:
    return value


def deserialize_json(data: str) -> ChannelStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChannelStatus value: {data!r}")
    return cast(ChannelStatus, data)
