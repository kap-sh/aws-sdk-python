"""Generated from Smithy shape ``com.amazonaws.connect#VocabularyLanguageCode``."""

from typing import Literal, TypeAlias, cast

VocabularyLanguageCode: TypeAlias = Literal[
    "ar-AE",
    "de-CH",
    "de-DE",
    "en-AB",
    "en-AU",
    "en-GB",
    "en-IE",
    "en-IN",
    "en-US",
    "en-WL",
    "es-ES",
    "es-US",
    "fr-CA",
    "fr-FR",
    "hi-IN",
    "it-IT",
    "ja-JP",
    "ko-KR",
    "pt-BR",
    "pt-PT",
    "zh-CN",
    "en-NZ",
    "en-ZA",
    "ca-ES",
    "da-DK",
    "fi-FI",
    "id-ID",
    "ms-MY",
    "nl-NL",
    "no-NO",
    "pl-PL",
    "sv-SE",
    "tl-PH",
]


# --- restJson1 ser/de ---
def serialize_json(value: VocabularyLanguageCode) -> str:
    return value


def deserialize_json(data: str) -> VocabularyLanguageCode:
    return cast(VocabularyLanguageCode, data)
