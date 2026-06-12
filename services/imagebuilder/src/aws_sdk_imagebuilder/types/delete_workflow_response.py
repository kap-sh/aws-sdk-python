"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DeleteWorkflowResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.workflow_build_version_arn


class DeleteWorkflowResponse(TypedDict):
    workflow_build_version_arn: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_build_version_arn.WorkflowBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the workflow resource that this request deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkflowResponse) -> dict:
    out: dict = {}
    if "workflow_build_version_arn" in value:
        out["workflowBuildVersionArn"] = value["workflow_build_version_arn"]
    return out


def deserialize_json(data: dict) -> DeleteWorkflowResponse:
    out: DeleteWorkflowResponse = {}  # type: ignore[typeddict-item]
    if "workflowBuildVersionArn" in data:
        out["workflow_build_version_arn"] = data["workflowBuildVersionArn"]
    return out
