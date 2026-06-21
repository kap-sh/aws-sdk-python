"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#Language``."""

from typing import Literal, TypeAlias, cast

"""Supported input languages"""
Language: TypeAlias = Literal[
    "EN",
    "DE",
    "ES",
    "FR",
    "IT",
    "PT",
    "JA",
    "KO",
    "CN",
    "TW",
    "HK",
]


# --- restJson1 ser/de ---
def serialize_json(value: Language) -> str:
    return value


def deserialize_json(data: str) -> Language:
    return cast(Language, data)
