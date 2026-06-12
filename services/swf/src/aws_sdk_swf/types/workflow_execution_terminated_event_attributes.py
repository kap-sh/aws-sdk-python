"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionTerminatedEventAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.child_policy
    import aws_sdk_swf.types.data
    import aws_sdk_swf.types.terminate_reason
    import aws_sdk_swf.types.workflow_execution_terminated_cause


class WorkflowExecutionTerminatedEventAttributes(TypedDict):
    reason: NotRequired["aws_sdk_swf.types.terminate_reason.TerminateReason"]
    """<p>The reason provided for the termination.</p>"""
    details: NotRequired["aws_sdk_swf.types.data.Data"]
    """<p>The details provided for the termination.</p>"""
    child_policy: "aws_sdk_swf.types.child_policy.ChildPolicy"
    """<p>The policy used for the child workflow executions of this workflow execution.</p> <p>The supported child policies are:</p> <ul> <li> <p> <code>TERMINATE</code> – The child executions are terminated.</p> </li> <li> <p> <code>REQUEST_CANCEL</code> – A request to cancel is attempted for each child execution by recording a <code>WorkflowExecutionCancelRequested</code> event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.</p> </li> <li> <p> <code>ABANDON</code> – No action is taken. The child executions continue to run.</p> </li> </ul>"""
    cause: NotRequired[
        "aws_sdk_swf.types.workflow_execution_terminated_cause.WorkflowExecutionTerminatedCause"
    ]
    """<p>If set, indicates that the workflow execution was automatically terminated, and specifies the cause. This happens if the parent workflow execution times out or is terminated and the child policy is set to terminate child executions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowExecutionTerminatedEventAttributes) -> dict:
    out: dict = {}
    if "reason" in value:
        out["reason"] = value["reason"]
    if "details" in value:
        out["details"] = value["details"]
    import aws_sdk_swf.types.child_policy

    out["childPolicy"] = aws_sdk_swf.types.child_policy.serialize_aws_json_1_0(
        value["child_policy"]
    )
    if "cause" in value:
        import aws_sdk_swf.types.workflow_execution_terminated_cause

        out["cause"] = (
            aws_sdk_swf.types.workflow_execution_terminated_cause.serialize_aws_json_1_0(
                value["cause"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowExecutionTerminatedEventAttributes:
    out: WorkflowExecutionTerminatedEventAttributes = {}  # type: ignore[typeddict-item]
    if "reason" in data:
        out["reason"] = data["reason"]
    if "details" in data:
        out["details"] = data["details"]
    if "childPolicy" in data:
        import aws_sdk_swf.types.child_policy

        out["child_policy"] = aws_sdk_swf.types.child_policy.deserialize_aws_json_1_0(
            data["childPolicy"]
        )
    else:
        raise DeserializationError(
            "WorkflowExecutionTerminatedEventAttributes.child_policy required"
        )
    if "cause" in data:
        import aws_sdk_swf.types.workflow_execution_terminated_cause

        out["cause"] = (
            aws_sdk_swf.types.workflow_execution_terminated_cause.deserialize_aws_json_1_0(
                data["cause"]
            )
        )
    return out
