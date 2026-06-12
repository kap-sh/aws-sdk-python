"""Generated from Smithy shape ``com.amazonaws.batch#ResourceRequirements``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.resource_requirement

ResourceRequirements: TypeAlias = list[
    "aws_sdk_batch.types.resource_requirement.ResourceRequirement"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceRequirements) -> list:
    import aws_sdk_batch.types.resource_requirement

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.resource_requirement.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceRequirements:
    import aws_sdk_batch.types.resource_requirement

    out: ResourceRequirements = []
    for item in data:
        out.append(aws_sdk_batch.types.resource_requirement.deserialize_json(item))
    return out
