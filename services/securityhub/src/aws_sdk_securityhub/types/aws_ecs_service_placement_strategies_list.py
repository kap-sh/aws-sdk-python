"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsServicePlacementStrategiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_service_placement_strategies_details

AwsEcsServicePlacementStrategiesList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ecs_service_placement_strategies_details.AwsEcsServicePlacementStrategiesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsServicePlacementStrategiesList) -> list:
    import aws_sdk_securityhub.types.aws_ecs_service_placement_strategies_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_service_placement_strategies_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEcsServicePlacementStrategiesList:
    import aws_sdk_securityhub.types.aws_ecs_service_placement_strategies_details

    out: AwsEcsServicePlacementStrategiesList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_service_placement_strategies_details.deserialize_json(
                item
            )
        )
    return out
