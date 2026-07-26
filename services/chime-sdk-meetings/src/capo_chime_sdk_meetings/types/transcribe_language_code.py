"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribeLanguageCode``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: TranscribeLanguageCode) -> str:
    return value


def deserialize_json(data: str) -> TranscribeLanguageCode:
    return cast(TranscribeLanguageCode, data)
