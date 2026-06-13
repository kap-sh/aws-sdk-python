"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteDatasetRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.dataset_id
    import aws_sdk_bedrock_agentcore_control.types.dataset_version

class DeleteDatasetRequest(TypedDict):
    dataset_id: "aws_sdk_bedrock_agentcore_control.types.dataset_id.DatasetId"
    """<p> The unique identifier of the dataset to delete. </p>"""
    dataset_version: NotRequired["aws_sdk_bedrock_agentcore_control.types.dataset_version.DatasetVersion"]
    """<p> Optional version to delete. If absent, deletes the entire dataset. If provided, deletes only that specific version. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteDatasetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDatasetRequest:
    out: DeleteDatasetRequest = {}  # type: ignore[typeddict-item]
    return out