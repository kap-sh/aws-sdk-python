"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#Locale``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_model_building_service.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: Locale) -> str:
    return value


def deserialize_json(data: str) -> Locale:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Locale value: {data!r}")
    return cast(Locale, data)
