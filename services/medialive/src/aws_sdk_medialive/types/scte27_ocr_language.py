"""Generated from Smithy shape ``com.amazonaws.medialive#Scte27OcrLanguage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Scte27 Ocr Language"""
Scte27OcrLanguage: TypeAlias = Literal[
    "DEU",
    "ENG",
    "FRA",
    "NLD",
    "POR",
    "SPA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEU",
        "ENG",
        "FRA",
        "NLD",
        "POR",
        "SPA",
    )
)


def serialize_json(value: Scte27OcrLanguage) -> str:
    return value


def deserialize_json(data: str) -> Scte27OcrLanguage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Scte27OcrLanguage value: {data!r}")
    return cast(Scte27OcrLanguage, data)
