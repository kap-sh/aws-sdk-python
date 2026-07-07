"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionCanceledEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_swf.types.data
    import aws_sdk_swf.types.event_id


class WorkflowExecutionCanceledEventAttributes(TypedDict, closed=True):
    details: NotRequired["aws_sdk_swf.types.data.Data"]
    """<p>The details of the cancellation.</p>"""
    decision_task_completed_event_id: "aws_sdk_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskCompleted</code> event corresponding to the decision task that resulted in the <code>CancelWorkflowExecution</code> decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowExecutionCanceledEventAttributes) -> dict:
    out: dict = {}
    if "details" in value:
        out["details"] = value["details"]
    out["decisionTaskCompletedEventId"] = value.get(
        "decision_task_completed_event_id", 0
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowExecutionCanceledEventAttributes:
    out: WorkflowExecutionCanceledEventAttributes = {}  # type: ignore[typeddict-item]
    if "details" in data:
        out["details"] = data["details"]
    if "decisionTaskCompletedEventId" in data:
        out["decision_task_completed_event_id"] = data["decisionTaskCompletedEventId"]
    else:
        out["decision_task_completed_event_id"] = 0
    return out
