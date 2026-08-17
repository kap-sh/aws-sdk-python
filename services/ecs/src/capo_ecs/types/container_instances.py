"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerInstances``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.container_instance

ContainerInstances: TypeAlias = list[
    "capo_ecs.types.container_instance.ContainerInstance"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerInstances) -> list:
    import capo_ecs.types.container_instance

    out: list = []
    for item in value:
        out.append(capo_ecs.types.container_instance.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerInstances:
    import capo_ecs.types.container_instance

    out: ContainerInstances = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.container_instance.deserialize_aws_json_1_1(item))
    return out
