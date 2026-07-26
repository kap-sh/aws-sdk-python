"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerInstanceFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.container_instance_field

ContainerInstanceFieldList: TypeAlias = list[
    "capo_ecs.types.container_instance_field.ContainerInstanceField"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerInstanceFieldList) -> list:
    import capo_ecs.types.container_instance_field

    out: list = []
    for item in value:
        out.append(capo_ecs.types.container_instance_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerInstanceFieldList:
    import capo_ecs.types.container_instance_field

    out: ContainerInstanceFieldList = []
    for item in data:
        out.append(
            capo_ecs.types.container_instance_field.deserialize_aws_json_1_1(item)
        )
    return out
