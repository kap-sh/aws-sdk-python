"""Generated from Smithy shape ``com.amazonaws.medialive#Scte27OcrLanguage``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: Scte27OcrLanguage) -> str:
    return value


def deserialize_json(data: str) -> Scte27OcrLanguage:
    return cast(Scte27OcrLanguage, data)
