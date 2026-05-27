"""Generated from Smithy shape ``com.amazonaws.ecs#TaskManagedEBSVolumeTerminationPolicy``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_boolean


class TaskManagedEBSVolumeTerminationPolicy(TypedDict):
    delete_on_termination: "aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"
    """<p>Indicates whether the volume should be deleted on when the task stops. If a value of <code>true</code> is specified, Amazon ECS deletes the Amazon EBS volume on your behalf when the task goes into the <code>STOPPED</code> state. If no value is specified, the default value is <code>true</code> is used. When set to <code>false</code>, Amazon ECS leaves the volume in your account.</p>"""
