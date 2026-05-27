"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHookDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.deployment_lifecycle_hook_action
    import aws_sdk_ecs.types.deployment_lifecycle_hook_status
    import aws_sdk_ecs.types.deployment_lifecycle_hook_target_type
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class DeploymentLifecycleHookDetail(TypedDict):
    hook_id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ID of the lifecycle hook. Use this value when calling <code>ContinueServiceDeployment</code> to continue or roll back a paused deployment.</p>"""
    target_type: NotRequired[
        "aws_sdk_ecs.types.deployment_lifecycle_hook_target_type.DeploymentLifecycleHookTargetType"
    ]
    """<p>The type of action the lifecycle hook performs, such as <code>AWS_LAMBDA</code> or <code>PAUSE</code>.</p>"""
    target_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the hook target. For <code>AWS_LAMBDA</code> hooks, this is the Lambda function ARN. For <code>PAUSE</code> hooks, this field is not set.</p>"""
    status: NotRequired[
        "aws_sdk_ecs.types.deployment_lifecycle_hook_status.DeploymentLifecycleHookStatus"
    ]
    """<p>The status of the lifecycle hook. Valid values depend on the hook type:</p> <ul> <li> <p>For <code>AWS_LAMBDA</code> hooks: <code>IN_PROGRESS</code>, <code>SUCCEEDED</code>, <code>FAILED</code>, and <code>TIMED_OUT</code>.</p> </li> <li> <p>For <code>PAUSE</code> hooks: <code>AWAITING_ACTION</code>, <code>SUCCEEDED</code>, <code>FAILED</code>, and <code>TIMED_OUT</code>.</p> </li> </ul>"""
    expires_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time when the lifecycle hook times out. If the hook has not been completed by this time, Amazon ECS takes the timeout action.</p>"""
    timeout_action: NotRequired[
        "aws_sdk_ecs.types.deployment_lifecycle_hook_action.DeploymentLifecycleHookAction"
    ]
    """<p>The action Amazon ECS takes when the lifecycle hook times out. Valid values are <code>CONTINUE</code> and <code>ROLLBACK</code>.</p>"""
