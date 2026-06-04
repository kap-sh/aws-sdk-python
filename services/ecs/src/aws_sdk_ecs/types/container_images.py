"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerImages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container_image

ContainerImages: TypeAlias = list["aws_sdk_ecs.types.container_image.ContainerImage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerImages) -> list:
    import aws_sdk_ecs.types.container_image

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.container_image.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerImages:
    import aws_sdk_ecs.types.container_image

    out: ContainerImages = []
    for item in data:
        out.append(aws_sdk_ecs.types.container_image.deserialize_aws_json_1_1(item))
    return out
