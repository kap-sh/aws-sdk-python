"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsServicePlacementConstraintsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_service_placement_constraints_details

AwsEcsServicePlacementConstraintsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ecs_service_placement_constraints_details.AwsEcsServicePlacementConstraintsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsServicePlacementConstraintsList) -> list:
    import aws_sdk_securityhub.types.aws_ecs_service_placement_constraints_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_service_placement_constraints_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEcsServicePlacementConstraintsList:
    import aws_sdk_securityhub.types.aws_ecs_service_placement_constraints_details

    out: AwsEcsServicePlacementConstraintsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_service_placement_constraints_details.deserialize_json(
                item
            )
        )
    return out
