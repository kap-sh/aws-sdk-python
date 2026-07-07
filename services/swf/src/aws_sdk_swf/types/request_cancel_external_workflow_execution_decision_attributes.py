"""Generated from Smithy shape ``com.amazonaws.swf#RequestCancelExternalWorkflowExecutionDecisionAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.data
    import aws_sdk_swf.types.workflow_id
    import aws_sdk_swf.types.workflow_run_id_optional


class RequestCancelExternalWorkflowExecutionDecisionAttributes(TypedDict, closed=True):
    workflow_id: "aws_sdk_swf.types.workflow_id.WorkflowId"
    """<p> The <code>workflowId</code> of the external workflow execution to cancel.</p>"""
    run_id: NotRequired[
        "aws_sdk_swf.types.workflow_run_id_optional.WorkflowRunIdOptional"
    ]
    """<p>The <code>runId</code> of the external workflow execution to cancel.</p>"""
    control: NotRequired["aws_sdk_swf.types.data.Data"]
    """<p>The data attached to the event that can be used by the decider in subsequent workflow tasks.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: RequestCancelExternalWorkflowExecutionDecisionAttributes,
) -> dict:
    out: dict = {}
    out["workflowId"] = value["workflow_id"]
    if "run_id" in value:
        out["runId"] = value["run_id"]
    if "control" in value:
        out["control"] = value["control"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> RequestCancelExternalWorkflowExecutionDecisionAttributes:
    out: RequestCancelExternalWorkflowExecutionDecisionAttributes = {}  # type: ignore[typeddict-item]
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    else:
        raise DeserializationError(
            "RequestCancelExternalWorkflowExecutionDecisionAttributes.workflow_id required"
        )
    if "runId" in data:
        out["run_id"] = data["runId"]
    if "control" in data:
        out["control"] = data["control"]
    return out
