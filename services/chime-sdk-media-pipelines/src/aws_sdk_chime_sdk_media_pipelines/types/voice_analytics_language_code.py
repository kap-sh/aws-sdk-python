"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#VoiceAnalyticsLanguageCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

VoiceAnalyticsLanguageCode: TypeAlias = Literal["en-US",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("en-US",))


def serialize_json(value: VoiceAnalyticsLanguageCode) -> str:
    return value


def deserialize_json(data: str) -> VoiceAnalyticsLanguageCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown VoiceAnalyticsLanguageCode value: {data!r}"
        )
    return cast(VoiceAnalyticsLanguageCode, data)
