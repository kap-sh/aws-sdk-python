"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerImages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.container_image

ContainerImages: TypeAlias = list["capo_ecs.types.container_image.ContainerImage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerImages) -> list:
    import capo_ecs.types.container_image

    out: list = []
    for item in value:
        out.append(capo_ecs.types.container_image.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerImages:
    import capo_ecs.types.container_image

    out: ContainerImages = []
    for item in data:
        out.append(capo_ecs.types.container_image.deserialize_aws_json_1_1(item))
    return out
