"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CallAnalyticsLanguageCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "en-US",
        "en-GB",
        "es-US",
        "fr-CA",
        "fr-FR",
        "en-AU",
        "it-IT",
        "de-DE",
        "pt-BR",
    )
)


def serialize_json(value: CallAnalyticsLanguageCode) -> str:
    return value


def deserialize_json(data: str) -> CallAnalyticsLanguageCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CallAnalyticsLanguageCode value: {data!r}")
    return cast(CallAnalyticsLanguageCode, data)
