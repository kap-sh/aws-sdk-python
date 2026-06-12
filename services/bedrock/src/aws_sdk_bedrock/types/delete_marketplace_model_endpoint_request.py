"""Generated from Smithy shape ``com.amazonaws.bedrock#DeleteMarketplaceModelEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.arn


class DeleteMarketplaceModelEndpointRequest(TypedDict):
    endpoint_arn: "aws_sdk_bedrock.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the endpoint you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMarketplaceModelEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMarketplaceModelEndpointRequest:
    out: DeleteMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
