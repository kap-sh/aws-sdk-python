"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeWorkflowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.described_workflow


class DescribeWorkflowResponse(TypedDict, closed=True):
    workflow: "capo_transfer.types.described_workflow.DescribedWorkflow"
    """<p>The structure that contains the details of the workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkflowResponse) -> dict:
    out: dict = {}
    import capo_transfer.types.described_workflow

    out["Workflow"] = capo_transfer.types.described_workflow.serialize_aws_json_1_1(
        value["workflow"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkflowResponse:
    out: DescribeWorkflowResponse = {}  # type: ignore[typeddict-item]
    if "Workflow" in data:
        import capo_transfer.types.described_workflow

        out["workflow"] = (
            capo_transfer.types.described_workflow.deserialize_aws_json_1_1(
                data["Workflow"]
            )
        )
    else:
        raise DeserializationError("DescribeWorkflowResponse.workflow required")
    return out
