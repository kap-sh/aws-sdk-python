"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeExecutionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.described_execution
    import aws_sdk_transfer.types.workflow_id


class DescribeExecutionResponse(TypedDict):
    workflow_id: "aws_sdk_transfer.types.workflow_id.WorkflowId"
    """<p>A unique identifier for the workflow.</p>"""
    execution: "aws_sdk_transfer.types.described_execution.DescribedExecution"
    """<p>The structure that contains the details of the workflow' execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExecutionResponse) -> dict:
    out: dict = {}
    out["WorkflowId"] = value["workflow_id"]
    import aws_sdk_transfer.types.described_execution

    out["Execution"] = (
        aws_sdk_transfer.types.described_execution.serialize_aws_json_1_1(
            value["execution"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExecutionResponse:
    out: DescribeExecutionResponse = {}  # type: ignore[typeddict-item]
    if "WorkflowId" in data:
        out["workflow_id"] = data["WorkflowId"]
    else:
        raise DeserializationError("DescribeExecutionResponse.workflow_id required")
    if "Execution" in data:
        import aws_sdk_transfer.types.described_execution

        out["execution"] = (
            aws_sdk_transfer.types.described_execution.deserialize_aws_json_1_1(
                data["Execution"]
            )
        )
    else:
        raise DeserializationError("DescribeExecutionResponse.execution required")
    return out
