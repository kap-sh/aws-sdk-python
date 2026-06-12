"""Generated from Smithy shape ``com.amazonaws.polly#LanguageCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_polly.errors import DeserializationError

LanguageCode: TypeAlias = Literal[
    "arb",
    "cmn-CN",
    "cy-GB",
    "da-DK",
    "de-DE",
    "en-AU",
    "en-GB",
    "en-GB-WLS",
    "en-IN",
    "en-US",
    "es-ES",
    "es-MX",
    "es-US",
    "fr-CA",
    "fr-FR",
    "is-IS",
    "it-IT",
    "ja-JP",
    "hi-IN",
    "ko-KR",
    "nb-NO",
    "nl-NL",
    "pl-PL",
    "pt-BR",
    "pt-PT",
    "ro-RO",
    "ru-RU",
    "sv-SE",
    "tr-TR",
    "en-NZ",
    "en-ZA",
    "ca-ES",
    "de-AT",
    "yue-CN",
    "ar-AE",
    "fi-FI",
    "en-IE",
    "nl-BE",
    "fr-BE",
    "cs-CZ",
    "de-CH",
    "en-SG",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "arb",
        "cmn-CN",
        "cy-GB",
        "da-DK",
        "de-DE",
        "en-AU",
        "en-GB",
        "en-GB-WLS",
        "en-IN",
        "en-US",
        "es-ES",
        "es-MX",
        "es-US",
        "fr-CA",
        "fr-FR",
        "is-IS",
        "it-IT",
        "ja-JP",
        "hi-IN",
        "ko-KR",
        "nb-NO",
        "nl-NL",
        "pl-PL",
        "pt-BR",
        "pt-PT",
        "ro-RO",
        "ru-RU",
        "sv-SE",
        "tr-TR",
        "en-NZ",
        "en-ZA",
        "ca-ES",
        "de-AT",
        "yue-CN",
        "ar-AE",
        "fi-FI",
        "en-IE",
        "nl-BE",
        "fr-BE",
        "cs-CZ",
        "de-CH",
        "en-SG",
    )
)


def serialize_json(value: LanguageCode) -> str:
    return value


def deserialize_json(data: str) -> LanguageCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LanguageCode value: {data!r}")
    return cast(LanguageCode, data)
