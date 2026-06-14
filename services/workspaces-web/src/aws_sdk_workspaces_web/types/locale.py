"""Generated from Smithy shape ``com.amazonaws.workspacesweb#Locale``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_web.errors import DeserializationError

Locale: TypeAlias = Literal[
    "de-DE",
    "en-US",
    "es-ES",
    "fr-FR",
    "id-ID",
    "it-IT",
    "ja-JP",
    "ko-KR",
    "pt-BR",
    "zh-CN",
    "zh-TW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "de-DE",
        "en-US",
        "es-ES",
        "fr-FR",
        "id-ID",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "pt-BR",
        "zh-CN",
        "zh-TW",
    )
)


def serialize_json(value: Locale) -> str:
    return value


def deserialize_json(data: str) -> Locale:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Locale value: {data!r}")
    return cast(Locale, data)
