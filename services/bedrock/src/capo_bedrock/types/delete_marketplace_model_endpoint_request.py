"""Generated from Smithy shape ``com.amazonaws.bedrock#DeleteMarketplaceModelEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.arn


class DeleteMarketplaceModelEndpointRequest(TypedDict, closed=True):
    endpoint_arn: "capo_bedrock.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the endpoint you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMarketplaceModelEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMarketplaceModelEndpointRequest:
    out: DeleteMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
