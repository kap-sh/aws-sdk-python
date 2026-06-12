"""Generated from Smithy shape ``com.amazonaws.bedrock#DeregisterMarketplaceModelEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.arn


class DeregisterMarketplaceModelEndpointRequest(TypedDict):
    endpoint_arn: "aws_sdk_bedrock.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the endpoint you want to deregister.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterMarketplaceModelEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeregisterMarketplaceModelEndpointRequest:
    out: DeregisterMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
