"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#BlueprintStage``."""

from typing import Literal, TypeAlias, cast

"""Stage of the Blueprint"""
BlueprintStage: TypeAlias = Literal[
    "DEVELOPMENT",
    "LIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: BlueprintStage) -> str:
    return value


def deserialize_json(data: str) -> BlueprintStage:
    return cast(BlueprintStage, data)
