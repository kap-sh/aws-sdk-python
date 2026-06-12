"""Generated from Smithy shape ``com.amazonaws.eventbridge#PlacementConstraints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.placement_constraint

PlacementConstraints: TypeAlias = list[
    "aws_sdk_eventbridge.types.placement_constraint.PlacementConstraint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacementConstraints) -> list:
    import aws_sdk_eventbridge.types.placement_constraint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_eventbridge.types.placement_constraint.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PlacementConstraints:
    import aws_sdk_eventbridge.types.placement_constraint

    out: PlacementConstraints = []
    for item in data:
        out.append(
            aws_sdk_eventbridge.types.placement_constraint.deserialize_aws_json_1_1(
                item
            )
        )
    return out
