"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#BlueprintStageFilter``."""

from typing import Literal, TypeAlias, cast

"""Blueprint Stage filter"""
BlueprintStageFilter: TypeAlias = Literal[
    "DEVELOPMENT",
    "LIVE",
    "ALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: BlueprintStageFilter) -> str:
    return value


def deserialize_json(data: str) -> BlueprintStageFilter:
    return cast(BlueprintStageFilter, data)
