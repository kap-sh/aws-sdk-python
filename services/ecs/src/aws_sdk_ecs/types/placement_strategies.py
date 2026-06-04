"""Generated from Smithy shape ``com.amazonaws.ecs#PlacementStrategies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.placement_strategy

PlacementStrategies: TypeAlias = list[
    "aws_sdk_ecs.types.placement_strategy.PlacementStrategy"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacementStrategies) -> list:
    import aws_sdk_ecs.types.placement_strategy

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.placement_strategy.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PlacementStrategies:
    import aws_sdk_ecs.types.placement_strategy

    out: PlacementStrategies = []
    for item in data:
        out.append(aws_sdk_ecs.types.placement_strategy.deserialize_aws_json_1_1(item))
    return out
