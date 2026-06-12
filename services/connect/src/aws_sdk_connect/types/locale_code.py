"""Generated from Smithy shape ``com.amazonaws.connect#LocaleCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

"""<p>The locale code for localized content. Supported values include en_US, de_DE, es_ES, fr_FR, id_ID, it_IT, ja_JP, ko_KR, pt_BR, zh_CN, and zh_TW.</p>"""
LocaleCode: TypeAlias = Literal[
    "en_US",
    "de_DE",
    "es_ES",
    "fr_FR",
    "id_ID",
    "it_IT",
    "ja_JP",
    "ko_KR",
    "pt_BR",
    "zh_CN",
    "zh_TW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "en_US",
        "de_DE",
        "es_ES",
        "fr_FR",
        "id_ID",
        "it_IT",
        "ja_JP",
        "ko_KR",
        "pt_BR",
        "zh_CN",
        "zh_TW",
    )
)


def serialize_json(value: LocaleCode) -> str:
    return value


def deserialize_json(data: str) -> LocaleCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LocaleCode value: {data!r}")
    return cast(LocaleCode, data)
