"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionCompletedEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_swf.types.data
    import aws_sdk_swf.types.event_id


class WorkflowExecutionCompletedEventAttributes(TypedDict, closed=True):
    result: NotRequired["aws_sdk_swf.types.data.Data"]
    """<p>The result produced by the workflow execution upon successful completion.</p>"""
    decision_task_completed_event_id: "aws_sdk_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskCompleted</code> event corresponding to the decision task that resulted in the <code>CompleteWorkflowExecution</code> decision to complete this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowExecutionCompletedEventAttributes) -> dict:
    out: dict = {}
    if "result" in value:
        out["result"] = value["result"]
    out["decisionTaskCompletedEventId"] = value.get(
        "decision_task_completed_event_id", 0
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowExecutionCompletedEventAttributes:
    out: WorkflowExecutionCompletedEventAttributes = {}  # type: ignore[typeddict-item]
    if "result" in data:
        out["result"] = data["result"]
    if "decisionTaskCompletedEventId" in data:
        out["decision_task_completed_event_id"] = data["decisionTaskCompletedEventId"]
    else:
        out["decision_task_completed_event_id"] = 0
    return out
