"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#VoiceAnalyticsLanguageCode``."""

from typing import Literal, TypeAlias, cast

VoiceAnalyticsLanguageCode: TypeAlias = Literal["en-US",]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceAnalyticsLanguageCode) -> str:
    return value


def deserialize_json(data: str) -> VoiceAnalyticsLanguageCode:
    return cast(VoiceAnalyticsLanguageCode, data)
