"""Generated from Smithy shape ``com.amazonaws.connect#VideoCapability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

VideoCapability: TypeAlias = Literal["SEND",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SEND",))


def serialize_json(value: VideoCapability) -> str:
    return value


def deserialize_json(data: str) -> VideoCapability:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VideoCapability value: {data!r}")
    return cast(VideoCapability, data)
