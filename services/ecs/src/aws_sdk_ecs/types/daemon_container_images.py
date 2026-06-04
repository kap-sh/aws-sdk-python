"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonContainerImages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_container_image

DaemonContainerImages: TypeAlias = list[
    "aws_sdk_ecs.types.daemon_container_image.DaemonContainerImage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonContainerImages) -> list:
    import aws_sdk_ecs.types.daemon_container_image

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.daemon_container_image.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DaemonContainerImages:
    import aws_sdk_ecs.types.daemon_container_image

    out: DaemonContainerImages = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.daemon_container_image.deserialize_aws_json_1_1(item)
        )
    return out
