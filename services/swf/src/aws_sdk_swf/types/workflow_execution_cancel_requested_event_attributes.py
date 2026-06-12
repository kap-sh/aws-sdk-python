"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionCancelRequestedEventAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_swf.types.event_id
    import aws_sdk_swf.types.workflow_execution
    import aws_sdk_swf.types.workflow_execution_cancel_requested_cause


class WorkflowExecutionCancelRequestedEventAttributes(TypedDict):
    external_workflow_execution: NotRequired[
        "aws_sdk_swf.types.workflow_execution.WorkflowExecution"
    ]
    """<p>The external workflow execution for which the cancellation was requested.</p>"""
    external_initiated_event_id: "aws_sdk_swf.types.event_id.EventId"
    """<p>The ID of the <code>RequestCancelExternalWorkflowExecutionInitiated</code> event corresponding to the <code>RequestCancelExternalWorkflowExecution</code> decision to cancel this workflow execution.The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    cause: NotRequired[
        "aws_sdk_swf.types.workflow_execution_cancel_requested_cause.WorkflowExecutionCancelRequestedCause"
    ]
    """<p>If set, indicates that the request to cancel the workflow execution was automatically generated, and specifies the cause. This happens if the parent workflow execution times out or is terminated, and the child policy is set to cancel child executions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: WorkflowExecutionCancelRequestedEventAttributes,
) -> dict:
    out: dict = {}
    if "external_workflow_execution" in value:
        import aws_sdk_swf.types.workflow_execution

        out["externalWorkflowExecution"] = (
            aws_sdk_swf.types.workflow_execution.serialize_aws_json_1_0(
                value["external_workflow_execution"]
            )
        )
    out["externalInitiatedEventId"] = value.get("external_initiated_event_id", 0)
    if "cause" in value:
        import aws_sdk_swf.types.workflow_execution_cancel_requested_cause

        out["cause"] = (
            aws_sdk_swf.types.workflow_execution_cancel_requested_cause.serialize_aws_json_1_0(
                value["cause"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> WorkflowExecutionCancelRequestedEventAttributes:
    out: WorkflowExecutionCancelRequestedEventAttributes = {}  # type: ignore[typeddict-item]
    if "externalWorkflowExecution" in data:
        import aws_sdk_swf.types.workflow_execution

        out["external_workflow_execution"] = (
            aws_sdk_swf.types.workflow_execution.deserialize_aws_json_1_0(
                data["externalWorkflowExecution"]
            )
        )
    if "externalInitiatedEventId" in data:
        out["external_initiated_event_id"] = data["externalInitiatedEventId"]
    else:
        out["external_initiated_event_id"] = 0
    if "cause" in data:
        import aws_sdk_swf.types.workflow_execution_cancel_requested_cause

        out["cause"] = (
            aws_sdk_swf.types.workflow_execution_cancel_requested_cause.deserialize_aws_json_1_0(
                data["cause"]
            )
        )
    return out
