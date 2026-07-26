"""Generated from Smithy shape ``com.amazonaws.bedrock#MarketplaceModelEndpointSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.marketplace_model_endpoint_summary

MarketplaceModelEndpointSummaries: TypeAlias = list[
    "capo_bedrock.types.marketplace_model_endpoint_summary.MarketplaceModelEndpointSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MarketplaceModelEndpointSummaries) -> list:
    import capo_bedrock.types.marketplace_model_endpoint_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.marketplace_model_endpoint_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MarketplaceModelEndpointSummaries:
    import capo_bedrock.types.marketplace_model_endpoint_summary

    out: MarketplaceModelEndpointSummaries = []
    for item in data:
        out.append(
            capo_bedrock.types.marketplace_model_endpoint_summary.deserialize_json(item)
        )
    return out
