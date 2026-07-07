"""Generated from Smithy shape ``com.amazonaws.bedrock#UpdateMarketplaceModelEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.marketplace_model_endpoint


class UpdateMarketplaceModelEndpointResponse(TypedDict, closed=True):
    marketplace_model_endpoint: (
        "aws_sdk_bedrock.types.marketplace_model_endpoint.MarketplaceModelEndpoint"
    )
    """<p>Details about the updated endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMarketplaceModelEndpointResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.marketplace_model_endpoint

    out["marketplaceModelEndpoint"] = (
        aws_sdk_bedrock.types.marketplace_model_endpoint.serialize_json(
            value["marketplace_model_endpoint"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateMarketplaceModelEndpointResponse:
    out: UpdateMarketplaceModelEndpointResponse = {}  # type: ignore[typeddict-item]
    if "marketplaceModelEndpoint" in data:
        import aws_sdk_bedrock.types.marketplace_model_endpoint

        out["marketplace_model_endpoint"] = (
            aws_sdk_bedrock.types.marketplace_model_endpoint.deserialize_json(
                data["marketplaceModelEndpoint"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateMarketplaceModelEndpointResponse.marketplace_model_endpoint required"
        )
    return out
