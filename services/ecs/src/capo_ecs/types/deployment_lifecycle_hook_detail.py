"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHookDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.deployment_lifecycle_hook_action
    import capo_ecs.types.deployment_lifecycle_hook_status
    import capo_ecs.types.deployment_lifecycle_hook_target_type
    import capo_ecs.types.string
    import capo_ecs.types.timestamp


class DeploymentLifecycleHookDetail(TypedDict, closed=True):
    hook_id: NotRequired["capo_ecs.types.string.String"]
    """<p>The ID of the lifecycle hook. Use this value when calling <code>ContinueServiceDeployment</code> to continue or roll back a paused deployment.</p>"""
    target_type: NotRequired[
        "capo_ecs.types.deployment_lifecycle_hook_target_type.DeploymentLifecycleHookTargetType"
    ]
    """<p>The type of action the lifecycle hook performs, such as <code>AWS_LAMBDA</code> or <code>PAUSE</code>.</p>"""
    target_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the hook target. For <code>AWS_LAMBDA</code> hooks, this is the Lambda function ARN. For <code>PAUSE</code> hooks, this field is not set.</p>"""
    status: NotRequired[
        "capo_ecs.types.deployment_lifecycle_hook_status.DeploymentLifecycleHookStatus"
    ]
    """<p>The status of the lifecycle hook. Valid values include <code>AWAITING_ACTION</code>, <code>IN_PROGRESS</code>, <code>SUCCEEDED</code>, <code>FAILED</code>, and <code>TIMED_OUT</code>.</p>"""
    expires_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The time when the lifecycle hook times out. If the hook has not been completed by this time, Amazon ECS takes the timeout action.</p>"""
    timeout_action: NotRequired[
        "capo_ecs.types.deployment_lifecycle_hook_action.DeploymentLifecycleHookAction"
    ]
    """<p>The action Amazon ECS takes when the lifecycle hook times out. Valid values are <code>CONTINUE</code> and <code>ROLLBACK</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentLifecycleHookDetail) -> dict:
    out: dict = {}
    if "hook_id" in value:
        out["hookId"] = value["hook_id"]
    if "target_type" in value:
        import capo_ecs.types.deployment_lifecycle_hook_target_type

        out["targetType"] = (
            capo_ecs.types.deployment_lifecycle_hook_target_type.serialize_aws_json_1_1(
                value["target_type"]
            )
        )
    if "target_arn" in value:
        out["targetArn"] = value["target_arn"]
    if "status" in value:
        import capo_ecs.types.deployment_lifecycle_hook_status

        out["status"] = (
            capo_ecs.types.deployment_lifecycle_hook_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "expires_at" in value:
        import capo_ecs.types.timestamp

        out["expiresAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["expires_at"]
        )
    if "timeout_action" in value:
        import capo_ecs.types.deployment_lifecycle_hook_action

        out["timeoutAction"] = (
            capo_ecs.types.deployment_lifecycle_hook_action.serialize_aws_json_1_1(
                value["timeout_action"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentLifecycleHookDetail:
    out: DeploymentLifecycleHookDetail = {}  # type: ignore[typeddict-item]
    if data.get("hookId") is not None:
        out["hook_id"] = data["hookId"]
    if data.get("targetType") is not None:
        import capo_ecs.types.deployment_lifecycle_hook_target_type

        out["target_type"] = (
            capo_ecs.types.deployment_lifecycle_hook_target_type.deserialize_aws_json_1_1(
                data["targetType"]
            )
        )
    if data.get("targetArn") is not None:
        out["target_arn"] = data["targetArn"]
    if data.get("status") is not None:
        import capo_ecs.types.deployment_lifecycle_hook_status

        out["status"] = (
            capo_ecs.types.deployment_lifecycle_hook_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("expiresAt") is not None:
        import capo_ecs.types.timestamp

        out["expires_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["expiresAt"]
        )
    if data.get("timeoutAction") is not None:
        import capo_ecs.types.deployment_lifecycle_hook_action

        out["timeout_action"] = (
            capo_ecs.types.deployment_lifecycle_hook_action.deserialize_aws_json_1_1(
                data["timeoutAction"]
            )
        )
    return out
