"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormLanguageCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "de-DE",
        "en-US",
        "es-ES",
        "fr-FR",
        "it-IT",
        "pt-BR",
        "ja-JP",
        "ko-KR",
        "zh-CN",
    )
)


def serialize_json(value: EvaluationFormLanguageCode) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormLanguageCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EvaluationFormLanguageCode value: {data!r}"
        )
    return cast(EvaluationFormLanguageCode, data)
