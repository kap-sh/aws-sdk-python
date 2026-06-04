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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentLifecycleHookTimeoutConfiguration) -> dict:
    out: dict = {}
    if "timeout_in_minutes" in value:
        out["timeoutInMinutes"] = value["timeout_in_minutes"]
    if "action" in value:
        import aws_sdk_ecs.types.deployment_lifecycle_hook_action

        out["action"] = (
            aws_sdk_ecs.types.deployment_lifecycle_hook_action.serialize_aws_json_1_1(
                value["action"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentLifecycleHookTimeoutConfiguration:
    out: DeploymentLifecycleHookTimeoutConfiguration = {}  # type: ignore[typeddict-item]
    if "timeoutInMinutes" in data:
        out["timeout_in_minutes"] = data["timeoutInMinutes"]
    if "action" in data:
        import aws_sdk_ecs.types.deployment_lifecycle_hook_action

        out["action"] = (
            aws_sdk_ecs.types.deployment_lifecycle_hook_action.deserialize_aws_json_1_1(
                data["action"]
            )
        )
    return out
