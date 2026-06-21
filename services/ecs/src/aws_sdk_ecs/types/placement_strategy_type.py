"""Generated from Smithy shape ``com.amazonaws.ecs#PlacementStrategyType``."""

from typing import Literal, TypeAlias, cast

PlacementStrategyType: TypeAlias = Literal[
    "random",
    "spread",
    "binpack",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacementStrategyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlacementStrategyType:
    return cast(PlacementStrategyType, data)
