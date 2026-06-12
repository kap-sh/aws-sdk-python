"""Generated from Smithy shape ``com.amazonaws.swf#ExternalWorkflowExecutionSignaledEventAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.event_id
    import aws_sdk_swf.types.workflow_execution


class ExternalWorkflowExecutionSignaledEventAttributes(TypedDict):
    workflow_execution: "aws_sdk_swf.types.workflow_execution.WorkflowExecution"
    """<p>The external workflow execution that the signal was delivered to.</p>"""
    initiated_event_id: "aws_sdk_swf.types.event_id.EventId"
    """<p>The ID of the <code>SignalExternalWorkflowExecutionInitiated</code> event corresponding to the <code>SignalExternalWorkflowExecution</code> decision to request this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ExternalWorkflowExecutionSignaledEventAttributes,
) -> dict:
    out: dict = {}
    import aws_sdk_swf.types.workflow_execution

    out["workflowExecution"] = (
        aws_sdk_swf.types.workflow_execution.serialize_aws_json_1_0(
            value["workflow_execution"]
        )
    )
    out["initiatedEventId"] = value.get("initiated_event_id", 0)
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ExternalWorkflowExecutionSignaledEventAttributes:
    out: ExternalWorkflowExecutionSignaledEventAttributes = {}  # type: ignore[typeddict-item]
    if "workflowExecution" in data:
        import aws_sdk_swf.types.workflow_execution

        out["workflow_execution"] = (
            aws_sdk_swf.types.workflow_execution.deserialize_aws_json_1_0(
                data["workflowExecution"]
            )
        )
    else:
        raise DeserializationError(
            "ExternalWorkflowExecutionSignaledEventAttributes.workflow_execution required"
        )
    if "initiatedEventId" in data:
        out["initiated_event_id"] = data["initiatedEventId"]
    else:
        out["initiated_event_id"] = 0
    return out
