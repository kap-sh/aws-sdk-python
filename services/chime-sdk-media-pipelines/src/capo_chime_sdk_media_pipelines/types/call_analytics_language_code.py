"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CallAnalyticsLanguageCode``."""

from typing import Literal, TypeAlias, cast

CallAnalyticsLanguageCode: TypeAlias = Literal[
    "en-US",
    "en-GB",
    "es-US",
    "fr-CA",
    "fr-FR",
    "en-AU",
    "it-IT",
    "de-DE",
    "pt-BR",
]


# --- restJson1 ser/de ---
def serialize_json(value: CallAnalyticsLanguageCode) -> str:
    return value


def deserialize_json(data: str) -> CallAnalyticsLanguageCode:
    return cast(CallAnalyticsLanguageCode, data)
