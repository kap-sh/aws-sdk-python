"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#LanguageCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_voice.errors import DeserializationError

LanguageCode: TypeAlias = Literal["en-US",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("en-US",))


def serialize_json(value: LanguageCode) -> str:
    return value


def deserialize_json(data: str) -> LanguageCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LanguageCode value: {data!r}")
    return cast(LanguageCode, data)
