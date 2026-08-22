"""Generated from Smithy shape ``com.amazonaws.bedrock#GetMarketplaceModelEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.marketplace_model_endpoint


class GetMarketplaceModelEndpointResponse(TypedDict, closed=True):
    marketplace_model_endpoint: NotRequired[
        "capo_bedrock.types.marketplace_model_endpoint.MarketplaceModelEndpoint"
    ]
    """<p>Details about the requested endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMarketplaceModelEndpointResponse) -> dict:
    out: dict = {}
    if "marketplace_model_endpoint" in value:
        import capo_bedrock.types.marketplace_model_endpoint

        out["marketplaceModelEndpoint"] = (
            capo_bedrock.types.marketplace_model_endpoint.serialize_json(
                value["marketplace_model_endpoint"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMarketplaceModelEndpointResponse:
    out: GetMarketplaceModelEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("marketplaceModelEndpoint") is not None:
        import capo_bedrock.types.marketplace_model_endpoint

        out["marketplace_model_endpoint"] = (
            capo_bedrock.types.marketplace_model_endpoint.deserialize_json(
                data["marketplaceModelEndpoint"]
            )
        )
    return out
