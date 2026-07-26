"""Generated from Smithy shape ``com.amazonaws.swf#ChildWorkflowExecutionFailedEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.data
    import capo_swf.types.event_id
    import capo_swf.types.failure_reason
    import capo_swf.types.workflow_execution
    import capo_swf.types.workflow_type


class ChildWorkflowExecutionFailedEventAttributes(TypedDict, closed=True):
    workflow_execution: "capo_swf.types.workflow_execution.WorkflowExecution"
    """<p>The child workflow execution that failed.</p>"""
    workflow_type: "capo_swf.types.workflow_type.WorkflowType"
    """<p>The type of the child workflow execution.</p>"""
    reason: NotRequired["capo_swf.types.failure_reason.FailureReason"]
    """<p>The reason for the failure (if provided).</p>"""
    details: NotRequired["capo_swf.types.data.Data"]
    """<p>The details of the failure (if provided).</p>"""
    initiated_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>StartChildWorkflowExecutionInitiated</code> event corresponding to the <code>StartChildWorkflowExecution</code> <a>Decision</a> to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    started_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>ChildWorkflowExecutionStarted</code> event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ChildWorkflowExecutionFailedEventAttributes) -> dict:
    out: dict = {}
    import capo_swf.types.workflow_execution

    out["workflowExecution"] = capo_swf.types.workflow_execution.serialize_aws_json_1_0(
        value["workflow_execution"]
    )
    import capo_swf.types.workflow_type

    out["workflowType"] = capo_swf.types.workflow_type.serialize_aws_json_1_0(
        value["workflow_type"]
    )
    if "reason" in value:
        out["reason"] = value["reason"]
    if "details" in value:
        out["details"] = value["details"]
    out["initiatedEventId"] = value.get("initiated_event_id", 0)
    out["startedEventId"] = value.get("started_event_id", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> ChildWorkflowExecutionFailedEventAttributes:
    out: ChildWorkflowExecutionFailedEventAttributes = {}  # type: ignore[typeddict-item]
    if "workflowExecution" in data:
        import capo_swf.types.workflow_execution

        out["workflow_execution"] = (
            capo_swf.types.workflow_execution.deserialize_aws_json_1_0(
                data["workflowExecution"]
            )
        )
    else:
        raise DeserializationError(
            "ChildWorkflowExecutionFailedEventAttributes.workflow_execution required"
        )
    if "workflowType" in data:
        import capo_swf.types.workflow_type

        out["workflow_type"] = capo_swf.types.workflow_type.deserialize_aws_json_1_0(
            data["workflowType"]
        )
    else:
        raise DeserializationError(
            "ChildWorkflowExecutionFailedEventAttributes.workflow_type required"
        )
    if "reason" in data:
        out["reason"] = data["reason"]
    if "details" in data:
        out["details"] = data["details"]
    if "initiatedEventId" in data:
        out["initiated_event_id"] = data["initiatedEventId"]
    else:
        out["initiated_event_id"] = 0
    if "startedEventId" in data:
        out["started_event_id"] = data["startedEventId"]
    else:
        out["started_event_id"] = 0
    return out
