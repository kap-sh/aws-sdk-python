"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHookTimeoutConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.deployment_lifecycle_hook_action
    import aws_sdk_ecs.types.deployment_lifecycle_hook_duration


class DeploymentLifecycleHookTimeoutConfiguration(TypedDict):
    timeout_in_minutes: NotRequired[
        "aws_sdk_ecs.types.deployment_lifecycle_hook_duration.DeploymentLifecycleHookDuration"
    ]
    """<p>The number of minutes Amazon ECS waits for the lifecycle hook to complete before taking the timeout action.</p>"""
    action: NotRequired[
        "aws_sdk_ecs.types.deployment_lifecycle_hook_action.DeploymentLifecycleHookAction"
    ]
    """<p>The action Amazon ECS takes when the lifecycle hook times out. Valid values are:</p> <ul> <li> <p> <code>CONTINUE</code> - Proceeds the deployment to the next lifecycle stage.</p> </li> <li> <p> <code>ROLLBACK</code> - Rolls back the deployment to the previous service revision.</p> </li> </ul>"""
