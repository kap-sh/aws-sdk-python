"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#Locale``."""

from typing import Literal, TypeAlias, cast

Locale: TypeAlias = Literal[
    "de-DE",
    "en-AU",
    "en-GB",
    "en-IN",
    "en-US",
    "es-419",
    "es-ES",
    "es-US",
    "fr-FR",
    "fr-CA",
    "it-IT",
    "ja-JP",
    "ko-KR",
]


# --- restJson1 ser/de ---
def serialize_json(value: Locale) -> str:
    return value


def deserialize_json(data: str) -> Locale:
    return cast(Locale, data)
