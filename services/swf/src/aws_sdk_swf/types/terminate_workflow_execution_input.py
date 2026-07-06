"""Generated from Smithy shape ``com.amazonaws.swf#TerminateWorkflowExecutionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.child_policy
    import aws_sdk_swf.types.data
    import aws_sdk_swf.types.domain_name
    import aws_sdk_swf.types.terminate_reason
    import aws_sdk_swf.types.workflow_id
    import aws_sdk_swf.types.workflow_run_id_optional


class TerminateWorkflowExecutionInput(TypedDict, closed=True):
    domain: "aws_sdk_swf.types.domain_name.DomainName"
    """<p>The domain of the workflow execution to terminate.</p>"""
    workflow_id: "aws_sdk_swf.types.workflow_id.WorkflowId"
    """<p>The workflowId of the workflow execution to terminate.</p>"""
    run_id: NotRequired[
        "aws_sdk_swf.types.workflow_run_id_optional.WorkflowRunIdOptional"
    ]
    """<p>The runId of the workflow execution to terminate.</p>"""
    reason: NotRequired["aws_sdk_swf.types.terminate_reason.TerminateReason"]
    """<p> A descriptive reason for terminating the workflow execution.</p>"""
    details: NotRequired["aws_sdk_swf.types.data.Data"]
    """<p> Details for terminating the workflow execution.</p>"""
    child_policy: NotRequired["aws_sdk_swf.types.child_policy.ChildPolicy"]
    """<p>If set, specifies the policy to use for the child workflow executions of the workflow execution being terminated. This policy overrides the child policy specified for the workflow execution at registration time or when starting the execution.</p> <p>The supported child policies are:</p> <ul> <li> <p> <code>TERMINATE</code> – The child executions are terminated.</p> </li> <li> <p> <code>REQUEST_CANCEL</code> – A request to cancel is attempted for each child execution by recording a <code>WorkflowExecutionCancelRequested</code> event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.</p> </li> <li> <p> <code>ABANDON</code> – No action is taken. The child executions continue to run.</p> </li> </ul> <note> <p>A child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault is returned.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TerminateWorkflowExecutionInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    out["workflowId"] = value["workflow_id"]
    if "run_id" in value:
        out["runId"] = value["run_id"]
    if "reason" in value:
        out["reason"] = value["reason"]
    if "details" in value:
        out["details"] = value["details"]
    if "child_policy" in value:
        import aws_sdk_swf.types.child_policy

        out["childPolicy"] = aws_sdk_swf.types.child_policy.serialize_aws_json_1_0(
            value["child_policy"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TerminateWorkflowExecutionInput:
    out: TerminateWorkflowExecutionInput = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("TerminateWorkflowExecutionInput.domain required")
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    else:
        raise DeserializationError(
            "TerminateWorkflowExecutionInput.workflow_id required"
        )
    if "runId" in data:
        out["run_id"] = data["runId"]
    if "reason" in data:
        out["reason"] = data["reason"]
    if "details" in data:
        out["details"] = data["details"]
    if "childPolicy" in data:
        import aws_sdk_swf.types.child_policy

        out["child_policy"] = aws_sdk_swf.types.child_policy.deserialize_aws_json_1_0(
            data["childPolicy"]
        )
    return out
