"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DesiredModality``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

"""Desired Modality types"""
DesiredModality: TypeAlias = Literal[
    "IMAGE",
    "DOCUMENT",
    "AUDIO",
    "VIDEO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IMAGE",
        "DOCUMENT",
        "AUDIO",
        "VIDEO",
    )
)


def serialize_json(value: DesiredModality) -> str:
    return value


def deserialize_json(data: str) -> DesiredModality:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DesiredModality value: {data!r}")
    return cast(DesiredModality, data)
