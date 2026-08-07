"""Generated from Smithy shape ``com.amazonaws.cloudformation#HookResultSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.hook_failure_mode
    import capo_cloudformation.types.hook_invocation_id
    import capo_cloudformation.types.hook_invocation_point
    import capo_cloudformation.types.hook_result_id
    import capo_cloudformation.types.hook_status
    import capo_cloudformation.types.hook_status_reason
    import capo_cloudformation.types.hook_type_arn
    import capo_cloudformation.types.hook_type_configuration_version_id
    import capo_cloudformation.types.hook_type_name
    import capo_cloudformation.types.hook_type_version_id
    import capo_cloudformation.types.list_hook_results_target_type
    import capo_cloudformation.types.timestamp


class HookResultSummary(TypedDict, closed=True):
    hook_result_id: NotRequired[
        "capo_cloudformation.types.hook_invocation_id.HookInvocationId"
    ]
    """<p>The unique identifier for this Hook invocation result.</p>"""
    invocation_point: NotRequired[
        "capo_cloudformation.types.hook_invocation_point.HookInvocationPoint"
    ]
    """<p>The specific point in the provisioning process where the Hook is invoked.</p>"""
    failure_mode: NotRequired[
        "capo_cloudformation.types.hook_failure_mode.HookFailureMode"
    ]
    """<p>The failure mode of the invocation.</p>"""
    type_name: NotRequired["capo_cloudformation.types.hook_type_name.HookTypeName"]
    """<p>The name of the Hook that was invoked.</p>"""
    type_version_id: NotRequired[
        "capo_cloudformation.types.hook_type_version_id.HookTypeVersionId"
    ]
    """<p>The version of the Hook that was invoked.</p>"""
    type_configuration_version_id: NotRequired[
        "capo_cloudformation.types.hook_type_configuration_version_id.HookTypeConfigurationVersionId"
    ]
    """<p>The version of the Hook configuration.</p>"""
    status: NotRequired["capo_cloudformation.types.hook_status.HookStatus"]
    """<p>The status of the Hook invocation. The following statuses are possible:</p> <ul> <li> <p> <code>HOOK_IN_PROGRESS</code>: The Hook is currently running.</p> </li> <li> <p> <code>HOOK_COMPLETE_SUCCEEDED</code>: The Hook completed successfully.</p> </li> <li> <p> <code>HOOK_COMPLETE_FAILED</code>: The Hook completed but failed validation.</p> </li> <li> <p> <code>HOOK_FAILED</code>: The Hook encountered an error during execution.</p> </li> </ul>"""
    hook_status_reason: NotRequired[
        "capo_cloudformation.types.hook_status_reason.HookStatusReason"
    ]
    """<p>A description of the Hook results status. For example, if the Hook result is in a failed state, this may contain additional information for the failed state.</p>"""
    invoked_at: NotRequired["capo_cloudformation.types.timestamp.Timestamp"]
    """<p>The timestamp when the Hook was invoked.</p> <p>Only shown in responses when the request does not specify <code>TargetType</code> and <code>TargetId</code> filters.</p>"""
    target_type: NotRequired[
        "capo_cloudformation.types.list_hook_results_target_type.ListHookResultsTargetType"
    ]
    """<p>The target type that the Hook was invoked against.</p>"""
    target_id: NotRequired["capo_cloudformation.types.hook_result_id.HookResultId"]
    """<p>The unique identifier of the Hook invocation target.</p>"""
    type_arn: NotRequired["capo_cloudformation.types.hook_type_arn.HookTypeArn"]
    """<p>The ARN of the Hook that was invoked.</p>"""
    hook_execution_target: NotRequired[
        "capo_cloudformation.types.hook_result_id.HookResultId"
    ]
    """<p>The Amazon Resource Name (ARN) of the target stack or request token of the Cloud Control API operation.</p> <p>Only shown in responses when the request does not specify <code>TargetType</code> and <code>TargetId</code> filters.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: HookResultSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "hook_result_id" in value:
        pairs.append((f"{key_prefix}HookResultId", str(value["hook_result_id"])))
    if "invocation_point" in value:
        import capo_cloudformation.types.hook_invocation_point

        capo_cloudformation.types.hook_invocation_point.serialize_query(
            value["invocation_point"], pairs, f"{key_prefix}InvocationPoint"
        )
    if "failure_mode" in value:
        import capo_cloudformation.types.hook_failure_mode

        capo_cloudformation.types.hook_failure_mode.serialize_query(
            value["failure_mode"], pairs, f"{key_prefix}FailureMode"
        )
    if "type_name" in value:
        pairs.append((f"{key_prefix}TypeName", str(value["type_name"])))
    if "type_version_id" in value:
        pairs.append((f"{key_prefix}TypeVersionId", str(value["type_version_id"])))
    if "type_configuration_version_id" in value:
        pairs.append(
            (
                f"{key_prefix}TypeConfigurationVersionId",
                str(value["type_configuration_version_id"]),
            )
        )
    if "status" in value:
        import capo_cloudformation.types.hook_status

        capo_cloudformation.types.hook_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "hook_status_reason" in value:
        pairs.append(
            (f"{key_prefix}HookStatusReason", str(value["hook_status_reason"]))
        )
    if "invoked_at" in value:
        import capo_cloudformation.types.timestamp

        capo_cloudformation.types.timestamp.serialize_query(
            value["invoked_at"], pairs, f"{key_prefix}InvokedAt"
        )
    if "target_type" in value:
        import capo_cloudformation.types.list_hook_results_target_type

        capo_cloudformation.types.list_hook_results_target_type.serialize_query(
            value["target_type"], pairs, f"{key_prefix}TargetType"
        )
    if "target_id" in value:
        pairs.append((f"{key_prefix}TargetId", str(value["target_id"])))
    if "type_arn" in value:
        pairs.append((f"{key_prefix}TypeArn", str(value["type_arn"])))
    if "hook_execution_target" in value:
        pairs.append(
            (f"{key_prefix}HookExecutionTarget", str(value["hook_execution_target"]))
        )


def deserialize_query(el: Element) -> HookResultSummary:
    out: HookResultSummary = {}  # type: ignore[typeddict-item]
    child_hook_result_id = el.find("HookResultId")
    if child_hook_result_id is not None:
        out["hook_result_id"] = str(child_hook_result_id.text or "")
    child_invocation_point = el.find("InvocationPoint")
    if child_invocation_point is not None:
        import capo_cloudformation.types.hook_invocation_point

        out["invocation_point"] = (
            capo_cloudformation.types.hook_invocation_point.deserialize_query(
                child_invocation_point
            )
        )
    child_failure_mode = el.find("FailureMode")
    if child_failure_mode is not None:
        import capo_cloudformation.types.hook_failure_mode

        out["failure_mode"] = (
            capo_cloudformation.types.hook_failure_mode.deserialize_query(
                child_failure_mode
            )
        )
    child_type_name = el.find("TypeName")
    if child_type_name is not None:
        out["type_name"] = str(child_type_name.text or "")
    child_type_version_id = el.find("TypeVersionId")
    if child_type_version_id is not None:
        out["type_version_id"] = str(child_type_version_id.text or "")
    child_type_configuration_version_id = el.find("TypeConfigurationVersionId")
    if child_type_configuration_version_id is not None:
        out["type_configuration_version_id"] = str(
            child_type_configuration_version_id.text or ""
        )
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudformation.types.hook_status

        out["status"] = capo_cloudformation.types.hook_status.deserialize_query(
            child_status
        )
    child_hook_status_reason = el.find("HookStatusReason")
    if child_hook_status_reason is not None:
        out["hook_status_reason"] = str(child_hook_status_reason.text or "")
    child_invoked_at = el.find("InvokedAt")
    if child_invoked_at is not None:
        import capo_cloudformation.types.timestamp

        out["invoked_at"] = capo_cloudformation.types.timestamp.deserialize_query(
            child_invoked_at
        )
    child_target_type = el.find("TargetType")
    if child_target_type is not None:
        import capo_cloudformation.types.list_hook_results_target_type

        out["target_type"] = (
            capo_cloudformation.types.list_hook_results_target_type.deserialize_query(
                child_target_type
            )
        )
    child_target_id = el.find("TargetId")
    if child_target_id is not None:
        out["target_id"] = str(child_target_id.text or "")
    child_type_arn = el.find("TypeArn")
    if child_type_arn is not None:
        out["type_arn"] = str(child_type_arn.text or "")
    child_hook_execution_target = el.find("HookExecutionTarget")
    if child_hook_execution_target is not None:
        out["hook_execution_target"] = str(child_hook_execution_target.text or "")
    return out
