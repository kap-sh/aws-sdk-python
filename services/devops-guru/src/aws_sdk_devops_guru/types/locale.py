"""Generated from Smithy shape ``com.amazonaws.devopsguru#Locale``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: Locale) -> str:
    return value


def deserialize_json(data: str) -> Locale:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Locale value: {data!r}")
    return cast(Locale, data)
