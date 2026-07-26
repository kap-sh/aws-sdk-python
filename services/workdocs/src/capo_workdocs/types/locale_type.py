"""Generated from Smithy shape ``com.amazonaws.workdocs#LocaleType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: LocaleType) -> str:
    return value


def deserialize_json(data: str) -> LocaleType:
    return cast(LocaleType, data)
