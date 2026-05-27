"""Generated from Smithy shape ``com.amazonaws.ecs#ContinueServiceDeploymentRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.deployment_lifecycle_hook_action
    import aws_sdk_ecs.types.string


class ContinueServiceDeploymentRequest(TypedDict):
    service_deployment_arn: "aws_sdk_ecs.types.string.String"
    """<p>The ARN of the service deployment to continue or roll back.</p>"""
    hook_id: "aws_sdk_ecs.types.string.String"
    """<p>The ID of the paused lifecycle hook to act on. You can find the <code>hookId</code> by calling <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceDeployments.html\">DescribeServiceDeployments</a> and inspecting the <code>lifecycleHookDetails</code> field of the service deployment.</p>"""
    action: NotRequired[
        "aws_sdk_ecs.types.deployment_lifecycle_hook_action.DeploymentLifecycleHookAction"
    ]
    """<p>The action to take on the paused lifecycle hook. Valid values are:</p> <ul> <li> <p> <code>CONTINUE</code> - Proceeds the deployment to the next lifecycle stage.</p> </li> <li> <p> <code>ROLLBACK</code> - Rolls back the deployment to the previous service revision.</p> </li> </ul> <p>If no value is specified, the default action is <code>CONTINUE</code>.</p>"""
