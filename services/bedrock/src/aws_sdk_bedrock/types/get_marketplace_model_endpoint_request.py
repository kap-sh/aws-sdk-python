"""Generated from Smithy shape ``com.amazonaws.bedrock#GetMarketplaceModelEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.arn


class GetMarketplaceModelEndpointRequest(TypedDict):
    endpoint_arn: "aws_sdk_bedrock.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the endpoint you want to get information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMarketplaceModelEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMarketplaceModelEndpointRequest:
    out: GetMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
