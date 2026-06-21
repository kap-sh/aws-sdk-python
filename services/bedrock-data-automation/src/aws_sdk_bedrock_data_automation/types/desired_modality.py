"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DesiredModality``."""

from typing import Literal, TypeAlias, cast

"""Desired Modality types"""
DesiredModality: TypeAlias = Literal[
    "IMAGE",
    "DOCUMENT",
    "AUDIO",
    "VIDEO",
]


# --- restJson1 ser/de ---
def serialize_json(value: DesiredModality) -> str:
    return value


def deserialize_json(data: str) -> DesiredModality:
    return cast(DesiredModality, data)
