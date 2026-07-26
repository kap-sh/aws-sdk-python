"""Generated from Smithy shape ``com.amazonaws.ecs#InstanceGenerationSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.instance_generation

InstanceGenerationSet: TypeAlias = list[
    "capo_ecs.types.instance_generation.InstanceGeneration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGenerationSet) -> list:
    import capo_ecs.types.instance_generation

    out: list = []
    for item in value:
        out.append(capo_ecs.types.instance_generation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceGenerationSet:
    import capo_ecs.types.instance_generation

    out: InstanceGenerationSet = []
    for item in data:
        out.append(capo_ecs.types.instance_generation.deserialize_aws_json_1_1(item))
    return out
