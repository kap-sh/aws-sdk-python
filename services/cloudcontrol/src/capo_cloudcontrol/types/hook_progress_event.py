"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#HookProgressEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudcontrol.types.hook_failure_mode
    import capo_cloudcontrol.types.hook_invocation_point
    import capo_cloudcontrol.types.hook_status
    import capo_cloudcontrol.types.hook_type_arn
    import capo_cloudcontrol.types.status_message
    import capo_cloudcontrol.types.timestamp
    import capo_cloudcontrol.types.type_name
    import capo_cloudcontrol.types.type_version_id


class HookProgressEvent(TypedDict, closed=True):
    hook_type_name: NotRequired["capo_cloudcontrol.types.type_name.TypeName"]
    """<p>The type name of the Hook being invoked.</p>"""
    hook_type_version_id: NotRequired[
        "capo_cloudcontrol.types.type_version_id.TypeVersionId"
    ]
    """<p>The type version of the Hook being invoked.</p>"""
    hook_type_arn: NotRequired["capo_cloudcontrol.types.hook_type_arn.HookTypeArn"]
    """<p>The ARN of the Hook being invoked.</p>"""
    invocation_point: NotRequired[
        "capo_cloudcontrol.types.hook_invocation_point.HookInvocationPoint"
    ]
    """<p>States whether the Hook is invoked before or after resource provisioning.</p>"""
    hook_status: NotRequired["capo_cloudcontrol.types.hook_status.HookStatus"]
    """<p>The status of the Hook invocation. The following are potential statuses:</p> <ul> <li> <p> <code>HOOK_PENDING</code>: The Hook was added to the invocation plan, but not yet invoked.</p> </li> <li> <p> <code>HOOK_IN_PROGRESS</code>: The Hook was invoked, but hasn't completed.</p> </li> <li> <p> <code>HOOK_COMPLETE_SUCCEEDED</code>: The Hook invocation is complete with a successful result.</p> </li> <li> <p> <code>HOOK_COMPLETE_FAILED</code>: The Hook invocation is complete with a failed result.</p> </li> <li> <p> <code>HOOK_FAILED</code>: The Hook invocation didn't complete successfully.</p> </li> </ul>"""
    hook_event_time: NotRequired["capo_cloudcontrol.types.timestamp.Timestamp"]
    """<p>The time that the Hook invocation request initiated.</p>"""
    hook_status_message: NotRequired[
        "capo_cloudcontrol.types.status_message.StatusMessage"
    ]
    """<p>The message explaining the current Hook status.</p>"""
    failure_mode: NotRequired[
        "capo_cloudcontrol.types.hook_failure_mode.HookFailureMode"
    ]
    """<p>The failure mode of the invocation. The following are the potential statuses:</p> <ul> <li> <p> <code>FAIL</code>: This will fail the Hook invocation and the request associated with it.</p> </li> <li> <p> <code>WARN</code>: This will fail the Hook invocation, but not the request associated with it.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HookProgressEvent) -> dict:
    out: dict = {}
    if "hook_type_name" in value:
        out["HookTypeName"] = value["hook_type_name"]
    if "hook_type_version_id" in value:
        out["HookTypeVersionId"] = value["hook_type_version_id"]
    if "hook_type_arn" in value:
        out["HookTypeArn"] = value["hook_type_arn"]
    if "invocation_point" in value:
        out["InvocationPoint"] = value["invocation_point"]
    if "hook_status" in value:
        out["HookStatus"] = value["hook_status"]
    if "hook_event_time" in value:
        import capo_cloudcontrol.types.timestamp

        out["HookEventTime"] = capo_cloudcontrol.types.timestamp.serialize_aws_json_1_0(
            value["hook_event_time"]
        )
    if "hook_status_message" in value:
        out["HookStatusMessage"] = value["hook_status_message"]
    if "failure_mode" in value:
        out["FailureMode"] = value["failure_mode"]
    return out


def deserialize_aws_json_1_0(data: dict) -> HookProgressEvent:
    out: HookProgressEvent = {}  # type: ignore[typeddict-item]
    if "HookTypeName" in data:
        out["hook_type_name"] = data["HookTypeName"]
    if "HookTypeVersionId" in data:
        out["hook_type_version_id"] = data["HookTypeVersionId"]
    if "HookTypeArn" in data:
        out["hook_type_arn"] = data["HookTypeArn"]
    if "InvocationPoint" in data:
        out["invocation_point"] = data["InvocationPoint"]
    if "HookStatus" in data:
        out["hook_status"] = data["HookStatus"]
    if "HookEventTime" in data:
        import capo_cloudcontrol.types.timestamp

        out["hook_event_time"] = (
            capo_cloudcontrol.types.timestamp.deserialize_aws_json_1_0(
                data["HookEventTime"]
            )
        )
    if "HookStatusMessage" in data:
        out["hook_status_message"] = data["HookStatusMessage"]
    if "FailureMode" in data:
        out["failure_mode"] = data["FailureMode"]
    return out
