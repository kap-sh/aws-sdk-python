"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#Language``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: Language) -> str:
    return value


def deserialize_json(data: str) -> Language:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Language value: {data!r}")
    return cast(Language, data)
