"""Generated from Smithy shape ``com.amazonaws.chime#BotType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime.errors import DeserializationError

BotType: TypeAlias = Literal["ChatBot",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ChatBot",))


def serialize_json(value: BotType) -> str:
    return value


def deserialize_json(data: str) -> BotType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BotType value: {data!r}")
    return cast(BotType, data)
