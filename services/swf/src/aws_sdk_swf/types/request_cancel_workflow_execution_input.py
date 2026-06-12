"""Generated from Smithy shape ``com.amazonaws.swf#RequestCancelWorkflowExecutionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.domain_name
    import aws_sdk_swf.types.workflow_id
    import aws_sdk_swf.types.workflow_run_id_optional


class RequestCancelWorkflowExecutionInput(TypedDict):
    domain: "aws_sdk_swf.types.domain_name.DomainName"
    """<p>The name of the domain containing the workflow execution to cancel.</p>"""
    workflow_id: "aws_sdk_swf.types.workflow_id.WorkflowId"
    """<p>The workflowId of the workflow execution to cancel.</p>"""
    run_id: NotRequired[
        "aws_sdk_swf.types.workflow_run_id_optional.WorkflowRunIdOptional"
    ]
    """<p>The runId of the workflow execution to cancel.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RequestCancelWorkflowExecutionInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    out["workflowId"] = value["workflow_id"]
    if "run_id" in value:
        out["runId"] = value["run_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RequestCancelWorkflowExecutionInput:
    out: RequestCancelWorkflowExecutionInput = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError(
            "RequestCancelWorkflowExecutionInput.domain required"
        )
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    else:
        raise DeserializationError(
            "RequestCancelWorkflowExecutionInput.workflow_id required"
        )
    if "runId" in data:
        out["run_id"] = data["runId"]
    return out
