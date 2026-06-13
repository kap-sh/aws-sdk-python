"""Generated from Smithy shape ``com.amazonaws.freetier#LanguageCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_freetier.errors import DeserializationError

LanguageCode: TypeAlias = Literal[
    "en-US",
    "en-GB",
    "id-ID",
    "de-DE",
    "es-ES",
    "fr-FR",
    "ja-JP",
    "it-IT",
    "pt-PT",
    "ko-KR",
    "zh-CN",
    "zh-TW",
    "tr-TR",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "en-US",
        "en-GB",
        "id-ID",
        "de-DE",
        "es-ES",
        "fr-FR",
        "ja-JP",
        "it-IT",
        "pt-PT",
        "ko-KR",
        "zh-CN",
        "zh-TW",
        "tr-TR",
    )
)


def serialize_aws_json_1_0(value: LanguageCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LanguageCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LanguageCode value: {data!r}")
    return cast(LanguageCode, data)
