"""Generated from Smithy shape ``com.amazonaws.ecs#ResourceRequirements``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.resource_requirement

ResourceRequirements: TypeAlias = list[
    "aws_sdk_ecs.types.resource_requirement.ResourceRequirement"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceRequirements) -> list:
    import aws_sdk_ecs.types.resource_requirement

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.resource_requirement.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceRequirements:
    import aws_sdk_ecs.types.resource_requirement

    out: ResourceRequirements = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.resource_requirement.deserialize_aws_json_1_1(item)
        )
    return out
