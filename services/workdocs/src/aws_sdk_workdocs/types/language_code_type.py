"""Generated from Smithy shape ``com.amazonaws.workdocs#LanguageCodeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

LanguageCodeType: TypeAlias = Literal[
    "AR",
    "BG",
    "BN",
    "DA",
    "DE",
    "CS",
    "EL",
    "EN",
    "ES",
    "FA",
    "FI",
    "FR",
    "HI",
    "HU",
    "ID",
    "IT",
    "JA",
    "KO",
    "LT",
    "LV",
    "NL",
    "NO",
    "PT",
    "RO",
    "RU",
    "SV",
    "SW",
    "TH",
    "TR",
    "ZH",
    "DEFAULT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AR",
        "BG",
        "BN",
        "DA",
        "DE",
        "CS",
        "EL",
        "EN",
        "ES",
        "FA",
        "FI",
        "FR",
        "HI",
        "HU",
        "ID",
        "IT",
        "JA",
        "KO",
        "LT",
        "LV",
        "NL",
        "NO",
        "PT",
        "RO",
        "RU",
        "SV",
        "SW",
        "TH",
        "TR",
        "ZH",
        "DEFAULT",
    )
)


def serialize_json(value: LanguageCodeType) -> str:
    return value


def deserialize_json(data: str) -> LanguageCodeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LanguageCodeType value: {data!r}")
    return cast(LanguageCodeType, data)
