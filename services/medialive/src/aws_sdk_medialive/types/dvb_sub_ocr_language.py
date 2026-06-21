"""Generated from Smithy shape ``com.amazonaws.medialive#DvbSubOcrLanguage``."""

from typing import Literal, TypeAlias, cast

"""Dvb Sub Ocr Language"""
DvbSubOcrLanguage: TypeAlias = Literal[
    "DEU",
    "ENG",
    "FRA",
    "NLD",
    "POR",
    "SPA",
]


# --- restJson1 ser/de ---
def serialize_json(value: DvbSubOcrLanguage) -> str:
    return value


def deserialize_json(data: str) -> DvbSubOcrLanguage:
    return cast(DvbSubOcrLanguage, data)
