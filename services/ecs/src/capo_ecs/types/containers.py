"""Generated from Smithy shape ``com.amazonaws.ecs#Containers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.container

Containers: TypeAlias = list["capo_ecs.types.container.Container"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Containers) -> list:
    import capo_ecs.types.container

    out: list = []
    for item in value:
        out.append(capo_ecs.types.container.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Containers:
    import capo_ecs.types.container

    out: Containers = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.container.deserialize_aws_json_1_1(item))
    return out
