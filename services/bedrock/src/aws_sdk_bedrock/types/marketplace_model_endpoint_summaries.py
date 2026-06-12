"""Generated from Smithy shape ``com.amazonaws.bedrock#MarketplaceModelEndpointSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.marketplace_model_endpoint_summary

MarketplaceModelEndpointSummaries: TypeAlias = list[
    "aws_sdk_bedrock.types.marketplace_model_endpoint_summary.MarketplaceModelEndpointSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MarketplaceModelEndpointSummaries) -> list:
    import aws_sdk_bedrock.types.marketplace_model_endpoint_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.marketplace_model_endpoint_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MarketplaceModelEndpointSummaries:
    import aws_sdk_bedrock.types.marketplace_model_endpoint_summary

    out: MarketplaceModelEndpointSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.marketplace_model_endpoint_summary.deserialize_json(
                item
            )
        )
    return out
