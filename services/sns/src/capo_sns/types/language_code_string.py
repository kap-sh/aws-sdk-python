"""Generated from Smithy shape ``com.amazonaws.sns#LanguageCodeString``."""

from typing import Literal, TypeAlias, cast

from capo_sns._protocol.xml import Element

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
def to_query_text(value: LanguageCodeString) -> str:
    return value


def from_query_text(text: str) -> LanguageCodeString:
    return cast(LanguageCodeString, text)


def serialize_query(
    value: LanguageCodeString, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LanguageCodeString:
    return from_query_text(el.text or "")
