"""Generated from Smithy shape ``com.amazonaws.translate#DisplayLanguageCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_translate.errors import DeserializationError

DisplayLanguageCode: TypeAlias = Literal[
    "de",
    "en",
    "es",
    "fr",
    "it",
    "ja",
    "ko",
    "pt",
    "zh",
    "zh-TW",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "de",
        "en",
        "es",
        "fr",
        "it",
        "ja",
        "ko",
        "pt",
        "zh",
        "zh-TW",
    )
)


def serialize_aws_json_1_1(value: DisplayLanguageCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DisplayLanguageCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DisplayLanguageCode value: {data!r}")
    return cast(DisplayLanguageCode, data)
