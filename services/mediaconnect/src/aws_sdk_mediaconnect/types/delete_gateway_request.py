"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DeleteGatewayRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.gateway_arn


class DeleteGatewayRequest(TypedDict):
    gateway_arn: "aws_sdk_mediaconnect.types.gateway_arn.GatewayArn"
    """<p> The Amazon Resource Name (ARN) of the gateway that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGatewayRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGatewayRequest:
    out: DeleteGatewayRequest = {}  # type: ignore[typeddict-item]
    return out
