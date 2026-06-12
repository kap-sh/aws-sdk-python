"""Generated from Smithy shape ``com.amazonaws.medialive#DvbSubOcrLanguage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

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


def serialize_json(value: DvbSubOcrLanguage) -> str:
    return value


def deserialize_json(data: str) -> DvbSubOcrLanguage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DvbSubOcrLanguage value: {data!r}")
    return cast(DvbSubOcrLanguage, data)
