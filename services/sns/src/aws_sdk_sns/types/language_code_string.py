"""Generated from Smithy shape ``com.amazonaws.sns#LanguageCodeString``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import DeserializationError

"""Supported language code for sending OTP message"""
LanguageCodeString: TypeAlias = Literal[
    "en-US",
    "en-GB",
    "es-419",
    "es-ES",
    "de-DE",
    "fr-CA",
    "fr-FR",
    "it-IT",
    "ja-JP",
    "pt-BR",
    "kr-KR",
    "zh-CN",
    "zh-TW",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "en-US",
        "en-GB",
        "es-419",
        "es-ES",
        "de-DE",
        "fr-CA",
        "fr-FR",
        "it-IT",
        "ja-JP",
        "pt-BR",
        "kr-KR",
        "zh-CN",
        "zh-TW",
    )
)


def to_query_text(value: LanguageCodeString) -> str:
    return value


def from_query_text(text: str) -> LanguageCodeString:
    if text not in _VALUES:
        raise DeserializationError(f"unknown LanguageCodeString value: {text!r}")
    return cast(LanguageCodeString, text)


def serialize_query(
    value: LanguageCodeString, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LanguageCodeString:
    return from_query_text(el.text or "")
