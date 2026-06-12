"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeExecutionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.execution_id
    import aws_sdk_transfer.types.workflow_id


class DescribeExecutionRequest(TypedDict):
    execution_id: "aws_sdk_transfer.types.execution_id.ExecutionId"
    """<p>A unique identifier for the execution of a workflow.</p>"""
    workflow_id: "aws_sdk_transfer.types.workflow_id.WorkflowId"
    """<p>A unique identifier for the workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExecutionRequest) -> dict:
    out: dict = {}
    out["ExecutionId"] = value["execution_id"]
    out["WorkflowId"] = value["workflow_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExecutionRequest:
    out: DescribeExecutionRequest = {}  # type: ignore[typeddict-item]
    if "ExecutionId" in data:
        out["execution_id"] = data["ExecutionId"]
    else:
        raise DeserializationError("DescribeExecutionRequest.execution_id required")
    if "WorkflowId" in data:
        out["workflow_id"] = data["WorkflowId"]
    else:
        raise DeserializationError("DescribeExecutionRequest.workflow_id required")
    return out
