"""Generated from Smithy shape ``com.amazonaws.connect#ScreenShareCapability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ScreenShareCapability: TypeAlias = Literal["SEND",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SEND",))


def serialize_json(value: ScreenShareCapability) -> str:
    return value


def deserialize_json(data: str) -> ScreenShareCapability:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScreenShareCapability value: {data!r}")
    return cast(ScreenShareCapability, data)
