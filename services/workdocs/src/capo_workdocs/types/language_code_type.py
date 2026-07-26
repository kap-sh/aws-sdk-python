"""Generated from Smithy shape ``com.amazonaws.workdocs#LanguageCodeType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: LanguageCodeType) -> str:
    return value


def deserialize_json(data: str) -> LanguageCodeType:
    return cast(LanguageCodeType, data)
