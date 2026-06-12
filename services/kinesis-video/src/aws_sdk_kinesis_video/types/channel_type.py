"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ChannelType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video.errors import DeserializationError

ChannelType: TypeAlias = Literal[
    "SINGLE_MASTER",
    "FULL_MESH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE_MASTER",
        "FULL_MESH",
    )
)


def serialize_json(value: ChannelType) -> str:
    return value


def deserialize_json(data: str) -> ChannelType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChannelType value: {data!r}")
    return cast(ChannelType, data)
