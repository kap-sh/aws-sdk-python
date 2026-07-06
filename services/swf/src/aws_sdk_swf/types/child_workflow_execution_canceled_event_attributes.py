"""Generated from Smithy shape ``com.amazonaws.swf#ChildWorkflowExecutionCanceledEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.data
    import aws_sdk_swf.types.event_id
    import aws_sdk_swf.types.workflow_execution
    import aws_sdk_swf.types.workflow_type


class ChildWorkflowExecutionCanceledEventAttributes(TypedDict, closed=True):
    workflow_execution: "aws_sdk_swf.types.workflow_execution.WorkflowExecution"
    """<p>The child workflow execution that was canceled.</p>"""
    workflow_type: "aws_sdk_swf.types.workflow_type.WorkflowType"
    """<p>The type of the child workflow execution.</p>"""
    details: NotRequired["aws_sdk_swf.types.data.Data"]
    """<p>Details of the cancellation (if provided).</p>"""
    initiated_event_id: "aws_sdk_swf.types.event_id.EventId"
    """<p>The ID of the <code>StartChildWorkflowExecutionInitiated</code> event corresponding to the <code>StartChildWorkflowExecution</code> <a>Decision</a> to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    started_event_id: "aws_sdk_swf.types.event_id.EventId"
    """<p>The ID of the <code>ChildWorkflowExecutionStarted</code> event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ChildWorkflowExecutionCanceledEventAttributes,
) -> dict:
    out: dict = {}
    import aws_sdk_swf.types.workflow_execution

    out["workflowExecution"] = (
        aws_sdk_swf.types.workflow_execution.serialize_aws_json_1_0(
            value["workflow_execution"]
        )
    )
    import aws_sdk_swf.types.workflow_type

    out["workflowType"] = aws_sdk_swf.types.workflow_type.serialize_aws_json_1_0(
        value["workflow_type"]
    )
    if "details" in value:
        out["details"] = value["details"]
    out["initiatedEventId"] = value.get("initiated_event_id", 0)
    out["startedEventId"] = value.get("started_event_id", 0)
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ChildWorkflowExecutionCanceledEventAttributes:
    out: ChildWorkflowExecutionCanceledEventAttributes = {}  # type: ignore[typeddict-item]
    if "workflowExecution" in data:
        import aws_sdk_swf.types.workflow_execution

        out["workflow_execution"] = (
            aws_sdk_swf.types.workflow_execution.deserialize_aws_json_1_0(
                data["workflowExecution"]
            )
        )
    else:
        raise DeserializationError(
            "ChildWorkflowExecutionCanceledEventAttributes.workflow_execution required"
        )
    if "workflowType" in data:
        import aws_sdk_swf.types.workflow_type

        out["workflow_type"] = aws_sdk_swf.types.workflow_type.deserialize_aws_json_1_0(
            data["workflowType"]
        )
    else:
        raise DeserializationError(
            "ChildWorkflowExecutionCanceledEventAttributes.workflow_type required"
        )
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
