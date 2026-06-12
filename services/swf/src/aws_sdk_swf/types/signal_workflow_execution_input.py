"""Generated from Smithy shape ``com.amazonaws.swf#SignalWorkflowExecutionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.data
    import aws_sdk_swf.types.domain_name
    import aws_sdk_swf.types.signal_name
    import aws_sdk_swf.types.workflow_id
    import aws_sdk_swf.types.workflow_run_id_optional


class SignalWorkflowExecutionInput(TypedDict):
    domain: "aws_sdk_swf.types.domain_name.DomainName"
    """<p>The name of the domain containing the workflow execution to signal.</p>"""
    workflow_id: "aws_sdk_swf.types.workflow_id.WorkflowId"
    """<p>The workflowId of the workflow execution to signal.</p>"""
    run_id: NotRequired[
        "aws_sdk_swf.types.workflow_run_id_optional.WorkflowRunIdOptional"
    ]
    """<p>The runId of the workflow execution to signal.</p>"""
    signal_name: "aws_sdk_swf.types.signal_name.SignalName"
    """<p>The name of the signal. This name must be meaningful to the target workflow.</p>"""
    input: NotRequired["aws_sdk_swf.types.data.Data"]
    """<p>Data to attach to the <code>WorkflowExecutionSignaled</code> event in the target workflow execution's history.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SignalWorkflowExecutionInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    out["workflowId"] = value["workflow_id"]
    if "run_id" in value:
        out["runId"] = value["run_id"]
    out["signalName"] = value["signal_name"]
    if "input" in value:
        out["input"] = value["input"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SignalWorkflowExecutionInput:
    out: SignalWorkflowExecutionInput = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("SignalWorkflowExecutionInput.domain required")
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    else:
        raise DeserializationError("SignalWorkflowExecutionInput.workflow_id required")
    if "runId" in data:
        out["run_id"] = data["runId"]
    if "signalName" in data:
        out["signal_name"] = data["signalName"]
    else:
        raise DeserializationError("SignalWorkflowExecutionInput.signal_name required")
    if "input" in data:
        out["input"] = data["input"]
    return out
