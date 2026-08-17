"""Generated from Smithy shape ``com.amazonaws.ecs#ResourceRequirements``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.resource_requirement

ResourceRequirements: TypeAlias = list[
    "capo_ecs.types.resource_requirement.ResourceRequirement"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceRequirements) -> list:
    import capo_ecs.types.resource_requirement

    out: list = []
    for item in value:
        out.append(capo_ecs.types.resource_requirement.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceRequirements:
    import capo_ecs.types.resource_requirement

    out: ResourceRequirements = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.resource_requirement.deserialize_aws_json_1_1(item))
    return out
