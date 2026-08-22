"""Generated from Smithy shape ``com.amazonaws.bedrock#ListMarketplaceModelEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.marketplace_model_endpoint_summaries
    import capo_bedrock.types.pagination_token


class ListMarketplaceModelEndpointsResponse(TypedDict, closed=True):
    marketplace_model_endpoints: NotRequired[
        "capo_bedrock.types.marketplace_model_endpoint_summaries.MarketplaceModelEndpointSummaries"
    ]
    """<p>An array of endpoint summaries.</p>"""
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>The token for the next set of results. Use this token to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMarketplaceModelEndpointsResponse) -> dict:
    out: dict = {}
    if "marketplace_model_endpoints" in value:
        import capo_bedrock.types.marketplace_model_endpoint_summaries

        out["marketplaceModelEndpoints"] = (
            capo_bedrock.types.marketplace_model_endpoint_summaries.serialize_json(
                value["marketplace_model_endpoints"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMarketplaceModelEndpointsResponse:
    out: ListMarketplaceModelEndpointsResponse = {}  # type: ignore[typeddict-item]
    if data.get("marketplaceModelEndpoints") is not None:
        import capo_bedrock.types.marketplace_model_endpoint_summaries

        out["marketplace_model_endpoints"] = (
            capo_bedrock.types.marketplace_model_endpoint_summaries.deserialize_json(
                data["marketplaceModelEndpoints"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
