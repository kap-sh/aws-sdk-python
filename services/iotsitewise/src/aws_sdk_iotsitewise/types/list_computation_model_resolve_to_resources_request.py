"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListComputationModelResolveToResourcesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.max_results
    import aws_sdk_iotsitewise.types.next_token


class ListComputationModelResolveToResourcesRequest(TypedDict):
    computation_model_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the computation model for which to list resolved resources.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token used for the next set of paginated results.</p>"""
    max_results: NotRequired["aws_sdk_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results returned for each paginated request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComputationModelResolveToResourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListComputationModelResolveToResourcesRequest:
    out: ListComputationModelResolveToResourcesRequest = {}  # type: ignore[typeddict-item]
    return out
