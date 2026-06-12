"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribeLanguageCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_meetings.errors import DeserializationError

TranscribeLanguageCode: TypeAlias = Literal[
    "en-US",
    "en-GB",
    "es-US",
    "fr-CA",
    "fr-FR",
    "en-AU",
    "it-IT",
    "de-DE",
    "pt-BR",
    "ja-JP",
    "ko-KR",
    "zh-CN",
    "th-TH",
    "hi-IN",
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
        "ja-JP",
        "ko-KR",
        "zh-CN",
        "th-TH",
        "hi-IN",
    )
)


def serialize_json(value: TranscribeLanguageCode) -> str:
    return value


def deserialize_json(data: str) -> TranscribeLanguageCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TranscribeLanguageCode value: {data!r}")
    return cast(TranscribeLanguageCode, data)
