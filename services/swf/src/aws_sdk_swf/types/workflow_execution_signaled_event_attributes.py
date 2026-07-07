"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionSignaledEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.data
    import aws_sdk_swf.types.event_id
    import aws_sdk_swf.types.signal_name
    import aws_sdk_swf.types.workflow_execution


class WorkflowExecutionSignaledEventAttributes(TypedDict, closed=True):
    signal_name: "aws_sdk_swf.types.signal_name.SignalName"
    """<p>The name of the signal received. The decider can use the signal name and inputs to determine how to the process the signal.</p>"""
    input: NotRequired["aws_sdk_swf.types.data.Data"]
    """<p>The inputs provided with the signal. The decider can use the signal name and inputs to determine how to process the signal.</p>"""
    external_workflow_execution: NotRequired[
        "aws_sdk_swf.types.workflow_execution.WorkflowExecution"
    ]
    """<p>The workflow execution that sent the signal. This is set only of the signal was sent by another workflow execution.</p>"""
    external_initiated_event_id: "aws_sdk_swf.types.event_id.EventId"
    """<p>The ID of the <code>SignalExternalWorkflowExecutionInitiated</code> event corresponding to the <code>SignalExternalWorkflow</code> decision to signal this workflow execution.The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event. This field is set only if the signal was initiated by another workflow execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowExecutionSignaledEventAttributes) -> dict:
    out: dict = {}
    out["signalName"] = value["signal_name"]
    if "input" in value:
        out["input"] = value["input"]
    if "external_workflow_execution" in value:
        import aws_sdk_swf.types.workflow_execution

        out["externalWorkflowExecution"] = (
            aws_sdk_swf.types.workflow_execution.serialize_aws_json_1_0(
                value["external_workflow_execution"]
            )
        )
    out["externalInitiatedEventId"] = value.get("external_initiated_event_id", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowExecutionSignaledEventAttributes:
    out: WorkflowExecutionSignaledEventAttributes = {}  # type: ignore[typeddict-item]
    if "signalName" in data:
        out["signal_name"] = data["signalName"]
    else:
        raise DeserializationError(
            "WorkflowExecutionSignaledEventAttributes.signal_name required"
        )
    if "input" in data:
        out["input"] = data["input"]
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
    return out
