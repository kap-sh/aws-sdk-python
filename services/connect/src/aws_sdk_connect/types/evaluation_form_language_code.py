"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormLanguageCode``."""

from typing import Literal, TypeAlias, cast

EvaluationFormLanguageCode: TypeAlias = Literal[
    "de-DE",
    "en-US",
    "es-ES",
    "fr-FR",
    "it-IT",
    "pt-BR",
    "ja-JP",
    "ko-KR",
    "zh-CN",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormLanguageCode) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormLanguageCode:
    return cast(EvaluationFormLanguageCode, data)
