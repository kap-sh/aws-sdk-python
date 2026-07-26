"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerImageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.container_image

ContainerImageList: TypeAlias = list[
    "capo_lightsail.types.container_image.ContainerImage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerImageList) -> list:
    import capo_lightsail.types.container_image

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.container_image.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerImageList:
    import capo_lightsail.types.container_image

    out: ContainerImageList = []
    for item in data:
        out.append(capo_lightsail.types.container_image.deserialize_aws_json_1_1(item))
    return out
