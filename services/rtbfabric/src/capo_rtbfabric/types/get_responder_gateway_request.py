"""Generated from Smithy shape ``com.amazonaws.rtbfabric#GetResponderGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rtbfabric.types.gateway_id


class GetResponderGatewayRequest(TypedDict, closed=True):
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResponderGatewayRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResponderGatewayRequest:
    out: GetResponderGatewayRequest = {}  # type: ignore[typeddict-item]
    return out
