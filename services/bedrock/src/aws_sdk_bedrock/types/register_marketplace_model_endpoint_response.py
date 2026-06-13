"""Generated from Smithy shape ``com.amazonaws.bedrock#RegisterMarketplaceModelEndpointResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.marketplace_model_endpoint


class RegisterMarketplaceModelEndpointResponse(TypedDict):
    marketplace_model_endpoint: (
        "aws_sdk_bedrock.types.marketplace_model_endpoint.MarketplaceModelEndpoint"
    )
    """<p>Details about the registered endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterMarketplaceModelEndpointResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.marketplace_model_endpoint

    out["marketplaceModelEndpoint"] = (
        aws_sdk_bedrock.types.marketplace_model_endpoint.serialize_json(
            value["marketplace_model_endpoint"]
        )
    )
    return out


def deserialize_json(data: dict) -> RegisterMarketplaceModelEndpointResponse:
    out: RegisterMarketplaceModelEndpointResponse = {}  # type: ignore[typeddict-item]
    if "marketplaceModelEndpoint" in data:
        import aws_sdk_bedrock.types.marketplace_model_endpoint

        out["marketplace_model_endpoint"] = (
            aws_sdk_bedrock.types.marketplace_model_endpoint.deserialize_json(
                data["marketplaceModelEndpoint"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterMarketplaceModelEndpointResponse.marketplace_model_endpoint required"
        )
    return out
