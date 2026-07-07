"""Generated from Smithy shape ``com.amazonaws.rtbfabric#DeleteResponderGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.gateway_id


class DeleteResponderGatewayRequest(TypedDict, closed=True):
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResponderGatewayRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResponderGatewayRequest:
    out: DeleteResponderGatewayRequest = {}  # type: ignore[typeddict-item]
    return out
