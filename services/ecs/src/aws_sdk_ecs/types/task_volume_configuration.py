"""Generated from Smithy shape ``com.amazonaws.ecs#TaskVolumeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.ecs_volume_name
    import aws_sdk_ecs.types.task_managed_ebs_volume_configuration


class TaskVolumeConfiguration(TypedDict):
    name: "aws_sdk_ecs.types.ecs_volume_name.ECSVolumeName"
    """<p>The name of the volume. This value must match the volume name from the <code>Volume</code> object in the task definition.</p>"""
    managed_ebs_volume: NotRequired[
        "aws_sdk_ecs.types.task_managed_ebs_volume_configuration.TaskManagedEBSVolumeConfiguration"
    ]
    """<p>The configuration for the Amazon EBS volume that Amazon ECS creates and manages on your behalf. These settings are used to create each Amazon EBS volume, with one volume created for each task. The Amazon EBS volumes are visible in your account in the Amazon EC2 console once they are created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskVolumeConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "managed_ebs_volume" in value:
        import aws_sdk_ecs.types.task_managed_ebs_volume_configuration

        out["managedEBSVolume"] = (
            aws_sdk_ecs.types.task_managed_ebs_volume_configuration.serialize_aws_json_1_1(
                value["managed_ebs_volume"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskVolumeConfiguration:
    out: TaskVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("TaskVolumeConfiguration.name required")
    if "managedEBSVolume" in data:
        import aws_sdk_ecs.types.task_managed_ebs_volume_configuration

        out["managed_ebs_volume"] = (
            aws_sdk_ecs.types.task_managed_ebs_volume_configuration.deserialize_aws_json_1_1(
                data["managedEBSVolume"]
            )
        )
    return out
