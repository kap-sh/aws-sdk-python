"""Generated from Smithy shape ``com.amazonaws.swf#ExternalWorkflowExecutionCancelRequestedEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.event_id
    import capo_swf.types.workflow_execution


class ExternalWorkflowExecutionCancelRequestedEventAttributes(TypedDict, closed=True):
    workflow_execution: "capo_swf.types.workflow_execution.WorkflowExecution"
    """<p>The external workflow execution to which the cancellation request was delivered.</p>"""
    initiated_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>RequestCancelExternalWorkflowExecutionInitiated</code> event corresponding to the <code>RequestCancelExternalWorkflowExecution</code> decision to cancel this external workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ExternalWorkflowExecutionCancelRequestedEventAttributes,
) -> dict:
    out: dict = {}
    import capo_swf.types.workflow_execution

    out["workflowExecution"] = capo_swf.types.workflow_execution.serialize_aws_json_1_0(
        value["workflow_execution"]
    )
    out["initiatedEventId"] = value.get("initiated_event_id", 0)
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ExternalWorkflowExecutionCancelRequestedEventAttributes:
    out: ExternalWorkflowExecutionCancelRequestedEventAttributes = {}  # type: ignore[typeddict-item]
    if "workflowExecution" in data:
        import capo_swf.types.workflow_execution

        out["workflow_execution"] = (
            capo_swf.types.workflow_execution.deserialize_aws_json_1_0(
                data["workflowExecution"]
            )
        )
    else:
        raise DeserializationError(
            "ExternalWorkflowExecutionCancelRequestedEventAttributes.workflow_execution required"
        )
    if "initiatedEventId" in data:
        out["initiated_event_id"] = data["initiatedEventId"]
    else:
        out["initiated_event_id"] = 0
    return out
