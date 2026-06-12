"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ChannelRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video.errors import DeserializationError

ChannelRole: TypeAlias = Literal[
    "MASTER",
    "VIEWER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MASTER",
        "VIEWER",
    )
)


def serialize_json(value: ChannelRole) -> str:
    return value


def deserialize_json(data: str) -> ChannelRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChannelRole value: {data!r}")
    return cast(ChannelRole, data)
