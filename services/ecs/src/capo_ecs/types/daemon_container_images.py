"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonContainerImages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.daemon_container_image

DaemonContainerImages: TypeAlias = list[
    "capo_ecs.types.daemon_container_image.DaemonContainerImage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonContainerImages) -> list:
    import capo_ecs.types.daemon_container_image

    out: list = []
    for item in value:
        out.append(capo_ecs.types.daemon_container_image.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DaemonContainerImages:
    import capo_ecs.types.daemon_container_image

    out: DaemonContainerImages = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.daemon_container_image.deserialize_aws_json_1_1(item))
    return out
