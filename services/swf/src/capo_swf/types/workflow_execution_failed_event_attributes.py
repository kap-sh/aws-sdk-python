"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionFailedEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.data
    import capo_swf.types.event_id
    import capo_swf.types.failure_reason


class WorkflowExecutionFailedEventAttributes(TypedDict, closed=True):
    reason: NotRequired["capo_swf.types.failure_reason.FailureReason"]
    """<p>The descriptive reason provided for the failure.</p>"""
    details: NotRequired["capo_swf.types.data.Data"]
    """<p>The details of the failure.</p>"""
    decision_task_completed_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskCompleted</code> event corresponding to the decision task that resulted in the <code>FailWorkflowExecution</code> decision to fail this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowExecutionFailedEventAttributes) -> dict:
    out: dict = {}
    if "reason" in value:
        out["reason"] = value["reason"]
    if "details" in value:
        out["details"] = value["details"]
    out["decisionTaskCompletedEventId"] = value.get(
        "decision_task_completed_event_id", 0
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowExecutionFailedEventAttributes:
    out: WorkflowExecutionFailedEventAttributes = {}  # type: ignore[typeddict-item]
    if "reason" in data:
        out["reason"] = data["reason"]
    if "details" in data:
        out["details"] = data["details"]
    if "decisionTaskCompletedEventId" in data:
        out["decision_task_completed_event_id"] = data["decisionTaskCompletedEventId"]
    else:
        out["decision_task_completed_event_id"] = 0
    return out
