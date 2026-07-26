"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateMarketplaceModelEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.marketplace_model_endpoint


class CreateMarketplaceModelEndpointResponse(TypedDict, closed=True):
    marketplace_model_endpoint: (
        "capo_bedrock.types.marketplace_model_endpoint.MarketplaceModelEndpoint"
    )
    """<p>Details about the created endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMarketplaceModelEndpointResponse) -> dict:
    out: dict = {}
    import capo_bedrock.types.marketplace_model_endpoint

    out["marketplaceModelEndpoint"] = (
        capo_bedrock.types.marketplace_model_endpoint.serialize_json(
            value["marketplace_model_endpoint"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateMarketplaceModelEndpointResponse:
    out: CreateMarketplaceModelEndpointResponse = {}  # type: ignore[typeddict-item]
    if "marketplaceModelEndpoint" in data:
        import capo_bedrock.types.marketplace_model_endpoint

        out["marketplace_model_endpoint"] = (
            capo_bedrock.types.marketplace_model_endpoint.deserialize_json(
                data["marketplaceModelEndpoint"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMarketplaceModelEndpointResponse.marketplace_model_endpoint required"
        )
    return out
