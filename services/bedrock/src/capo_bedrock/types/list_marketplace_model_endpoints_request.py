"""Generated from Smithy shape ``com.amazonaws.bedrock#ListMarketplaceModelEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.max_results
    import capo_bedrock.types.model_source_identifier
    import capo_bedrock.types.pagination_token


class ListMarketplaceModelEndpointsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_bedrock.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. If more results are available, the operation returns a <code>NextToken</code> value.</p>"""
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>The token for the next set of results. You receive this token from a previous <code>ListMarketplaceModelEndpoints</code> call.</p>"""
    model_source_equals: NotRequired[
        "capo_bedrock.types.model_source_identifier.ModelSourceIdentifier"
    ]
    """<p>If specified, only endpoints for the given model source identifier are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMarketplaceModelEndpointsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMarketplaceModelEndpointsRequest:
    out: ListMarketplaceModelEndpointsRequest = {}  # type: ignore[typeddict-item]
    return out
