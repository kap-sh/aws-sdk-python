"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DeleteGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.gateway_arn


class DeleteGatewayRequest(TypedDict, closed=True):
    gateway_arn: "capo_mediaconnect.types.gateway_arn.GatewayArn"
    """<p> The Amazon Resource Name (ARN) of the gateway that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGatewayRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGatewayRequest:
    out: DeleteGatewayRequest = {}  # type: ignore[typeddict-item]
    return out
