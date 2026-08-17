"""Generated from Smithy shape ``com.amazonaws.ecs#TaskVolumeConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.task_volume_configuration

TaskVolumeConfigurations: TypeAlias = list[
    "capo_ecs.types.task_volume_configuration.TaskVolumeConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskVolumeConfigurations) -> list:
    import capo_ecs.types.task_volume_configuration

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.task_volume_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TaskVolumeConfigurations:
    import capo_ecs.types.task_volume_configuration

    out: TaskVolumeConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.task_volume_configuration.deserialize_aws_json_1_1(item)
        )
    return out
