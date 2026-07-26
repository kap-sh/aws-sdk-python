"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PlacementStrategies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.placement_strategy

PlacementStrategies: TypeAlias = list[
    "capo_cloudwatch_events.types.placement_strategy.PlacementStrategy"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacementStrategies) -> list:
    import capo_cloudwatch_events.types.placement_strategy

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_events.types.placement_strategy.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PlacementStrategies:
    import capo_cloudwatch_events.types.placement_strategy

    out: PlacementStrategies = []
    for item in data:
        out.append(
            capo_cloudwatch_events.types.placement_strategy.deserialize_aws_json_1_1(
                item
            )
        )
    return out
