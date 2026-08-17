"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHookTimeoutConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.deployment_lifecycle_hook_action
    import capo_ecs.types.deployment_lifecycle_hook_duration


class DeploymentLifecycleHookTimeoutConfiguration(TypedDict, closed=True):
    timeout_in_minutes: NotRequired[
        "capo_ecs.types.deployment_lifecycle_hook_duration.DeploymentLifecycleHookDuration"
    ]
    """<p>The number of minutes Amazon ECS waits for the lifecycle hook to complete before taking the timeout action.</p> <p>Default: 1440 (24 hours)</p>"""
    action: NotRequired[
        "capo_ecs.types.deployment_lifecycle_hook_action.DeploymentLifecycleHookAction"
    ]
    """<p>The action Amazon ECS takes when the lifecycle hook times out. Valid values are:</p> <ul> <li> <p> <code>CONTINUE</code> - Proceeds the deployment to the next lifecycle stage.</p> </li> <li> <p> <code>ROLLBACK</code> - Rolls back the deployment to the previous service revision.</p> </li> </ul> <p>Default: <code>ROLLBACK</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentLifecycleHookTimeoutConfiguration) -> dict:
    out: dict = {}
    if "timeout_in_minutes" in value:
        out["timeoutInMinutes"] = value["timeout_in_minutes"]
    if "action" in value:
        import capo_ecs.types.deployment_lifecycle_hook_action

        out["action"] = (
            capo_ecs.types.deployment_lifecycle_hook_action.serialize_aws_json_1_1(
                value["action"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentLifecycleHookTimeoutConfiguration:
    out: DeploymentLifecycleHookTimeoutConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("timeoutInMinutes") is not None:
        out["timeout_in_minutes"] = data["timeoutInMinutes"]
    if data.get("action") is not None:
        import capo_ecs.types.deployment_lifecycle_hook_action

        out["action"] = (
            capo_ecs.types.deployment_lifecycle_hook_action.deserialize_aws_json_1_1(
                data["action"]
            )
        )
    return out
