"""Generated from Smithy shape ``com.amazonaws.medialive#Fmp4TimedMetadataBehavior``."""

from typing import Literal, TypeAlias, cast

"""Fmp4 Timed Metadata Behavior"""
Fmp4TimedMetadataBehavior: TypeAlias = Literal[
    "NO_PASSTHROUGH",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: Fmp4TimedMetadataBehavior) -> str:
    return value


def deserialize_json(data: str) -> Fmp4TimedMetadataBehavior:
    return cast(Fmp4TimedMetadataBehavior, data)
