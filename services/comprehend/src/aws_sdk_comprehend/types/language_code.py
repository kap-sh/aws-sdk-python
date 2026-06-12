"""Generated from Smithy shape ``com.amazonaws.comprehend#LanguageCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

LanguageCode: TypeAlias = Literal[
    "en",
    "es",
    "fr",
    "de",
    "it",
    "pt",
    "ar",
    "hi",
    "ja",
    "ko",
    "zh",
    "zh-TW",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "en",
        "es",
        "fr",
        "de",
        "it",
        "pt",
        "ar",
        "hi",
        "ja",
        "ko",
        "zh",
        "zh-TW",
    )
)


def serialize_aws_json_1_1(value: LanguageCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LanguageCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LanguageCode value: {data!r}")
    return cast(LanguageCode, data)
