"""Generated from Smithy shape ``com.amazonaws.workspacesweb#Locale``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: Locale) -> str:
    return value


def deserialize_json(data: str) -> Locale:
    return cast(Locale, data)
