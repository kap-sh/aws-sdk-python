"""Generated from Smithy shape ``com.amazonaws.ecs#TaskOverride``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container_overrides
    import aws_sdk_ecs.types.ephemeral_storage
    import aws_sdk_ecs.types.inference_accelerator_overrides
    import aws_sdk_ecs.types.string


class TaskOverride(TypedDict):
    container_overrides: NotRequired[
        "aws_sdk_ecs.types.container_overrides.ContainerOverrides"
    ]
    """<p>One or more container overrides that are sent to a task.</p>"""
    cpu: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The CPU override for the task.</p>"""
    inference_accelerator_overrides: NotRequired[
        "aws_sdk_ecs.types.inference_accelerator_overrides.InferenceAcceleratorOverrides"
    ]
    """<p>The Elastic Inference accelerator override for the task.</p>"""
    execution_role_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the task execution role override for the task. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html\">Amazon ECS task execution IAM role</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    memory: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The memory override for the task.</p>"""
    task_role_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html\">IAM Role for Tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    ephemeral_storage: NotRequired[
        "aws_sdk_ecs.types.ephemeral_storage.EphemeralStorage"
    ]
    """<p>The ephemeral storage setting override for the task.</p> <note> <p>This parameter is only supported for tasks hosted on Fargate that use the following platform versions:</p> <ul> <li> <p>Linux platform version <code>1.4.0</code> or later.</p> </li> <li> <p>Windows platform version <code>1.0.0</code> or later.</p> </li> </ul> </note>"""
