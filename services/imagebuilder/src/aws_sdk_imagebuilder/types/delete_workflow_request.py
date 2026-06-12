"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DeleteWorkflowRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.workflow_build_version_arn


class DeleteWorkflowRequest(TypedDict):
    workflow_build_version_arn: (
        "aws_sdk_imagebuilder.types.workflow_build_version_arn.WorkflowBuildVersionArn"
    )
    """<p>The Amazon Resource Name (ARN) of the workflow resource to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkflowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkflowRequest:
    out: DeleteWorkflowRequest = {}  # type: ignore[typeddict-item]
    return out
