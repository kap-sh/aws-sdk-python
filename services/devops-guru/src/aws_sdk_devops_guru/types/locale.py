"""Generated from Smithy shape ``com.amazonaws.devopsguru#Locale``."""

from typing import Literal, TypeAlias, cast

Locale: TypeAlias = Literal[
    "DE_DE",
    "EN_US",
    "EN_GB",
    "ES_ES",
    "FR_FR",
    "IT_IT",
    "JA_JP",
    "KO_KR",
    "PT_BR",
    "ZH_CN",
    "ZH_TW",
]


# --- restJson1 ser/de ---
def serialize_json(value: Locale) -> str:
    return value


def deserialize_json(data: str) -> Locale:
    return cast(Locale, data)
