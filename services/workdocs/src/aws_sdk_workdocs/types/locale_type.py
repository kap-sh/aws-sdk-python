"""Generated from Smithy shape ``com.amazonaws.workdocs#LocaleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

LocaleType: TypeAlias = Literal[
    "en",
    "fr",
    "ko",
    "de",
    "es",
    "ja",
    "ru",
    "zh_CN",
    "zh_TW",
    "pt_BR",
    "default",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "en",
        "fr",
        "ko",
        "de",
        "es",
        "ja",
        "ru",
        "zh_CN",
        "zh_TW",
        "pt_BR",
        "default",
    )
)


def serialize_json(value: LocaleType) -> str:
    return value


def deserialize_json(data: str) -> LocaleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LocaleType value: {data!r}")
    return cast(LocaleType, data)
