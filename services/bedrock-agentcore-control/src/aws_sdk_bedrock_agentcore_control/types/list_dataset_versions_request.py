"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListDatasetVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.dataset_id


class ListDatasetVersionsRequest(TypedDict):
    dataset_id: "aws_sdk_bedrock_agentcore_control.types.dataset_id.DatasetId"
    """<p> The unique identifier of the dataset. </p>"""
    next_token: NotRequired["str"]
    """<p> The token for the next page of results. </p>"""
    max_results: NotRequired["int"]
    """<p> The maximum number of versions to return per page. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDatasetVersionsRequest:
    out: ListDatasetVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
