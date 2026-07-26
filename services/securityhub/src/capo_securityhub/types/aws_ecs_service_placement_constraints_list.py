"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsServicePlacementConstraintsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_service_placement_constraints_details

AwsEcsServicePlacementConstraintsList: TypeAlias = list[
    "capo_securityhub.types.aws_ecs_service_placement_constraints_details.AwsEcsServicePlacementConstraintsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsServicePlacementConstraintsList) -> list:
    import capo_securityhub.types.aws_ecs_service_placement_constraints_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ecs_service_placement_constraints_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEcsServicePlacementConstraintsList:
    import capo_securityhub.types.aws_ecs_service_placement_constraints_details

    out: AwsEcsServicePlacementConstraintsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ecs_service_placement_constraints_details.deserialize_json(
                item
            )
        )
    return out
