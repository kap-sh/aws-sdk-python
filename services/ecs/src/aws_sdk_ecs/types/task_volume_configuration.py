"""Generated from Smithy shape ``com.amazonaws.ecs#TaskVolumeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

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
