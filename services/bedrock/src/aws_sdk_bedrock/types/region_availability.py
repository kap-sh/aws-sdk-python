"""Generated from Smithy shape ``com.amazonaws.bedrock#RegionAvailability``."""

from typing import Literal, TypeAlias, cast

RegionAvailability: TypeAlias = Literal[
    "AVAILABLE",
    "NOT_AVAILABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: RegionAvailability) -> str:
    return value


def deserialize_json(data: str) -> RegionAvailability:
    return cast(RegionAvailability, data)
