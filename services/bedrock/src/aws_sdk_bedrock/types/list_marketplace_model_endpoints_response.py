"""Generated from Smithy shape ``com.amazonaws.bedrock#ListMarketplaceModelEndpointsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.marketplace_model_endpoint_summaries
    import aws_sdk_bedrock.types.pagination_token


class ListMarketplaceModelEndpointsResponse(TypedDict):
    marketplace_model_endpoints: NotRequired[
        "aws_sdk_bedrock.types.marketplace_model_endpoint_summaries.MarketplaceModelEndpointSummaries"
    ]
    """<p>An array of endpoint summaries.</p>"""
    next_token: NotRequired["aws_sdk_bedrock.types.pagination_token.PaginationToken"]
    """<p>The token for the next set of results. Use this token to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMarketplaceModelEndpointsResponse) -> dict:
    out: dict = {}
    if "marketplace_model_endpoints" in value:
        import aws_sdk_bedrock.types.marketplace_model_endpoint_summaries

        out["marketplaceModelEndpoints"] = (
            aws_sdk_bedrock.types.marketplace_model_endpoint_summaries.serialize_json(
                value["marketplace_model_endpoints"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMarketplaceModelEndpointsResponse:
    out: ListMarketplaceModelEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "marketplaceModelEndpoints" in data:
        import aws_sdk_bedrock.types.marketplace_model_endpoint_summaries

        out["marketplace_model_endpoints"] = (
            aws_sdk_bedrock.types.marketplace_model_endpoint_summaries.deserialize_json(
                data["marketplaceModelEndpoints"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
