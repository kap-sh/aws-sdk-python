"""Generated from Smithy shape ``com.amazonaws.ecs#TaskVolumeConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task_volume_configuration

TaskVolumeConfigurations: TypeAlias = list[
    "aws_sdk_ecs.types.task_volume_configuration.TaskVolumeConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskVolumeConfigurations) -> list:
    import aws_sdk_ecs.types.task_volume_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.task_volume_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TaskVolumeConfigurations:
    import aws_sdk_ecs.types.task_volume_configuration

    out: TaskVolumeConfigurations = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.task_volume_configuration.deserialize_aws_json_1_1(item)
        )
    return out
