"""Generated from Smithy shape ``com.amazonaws.rtbfabric#DeleteRequesterGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rtbfabric.types.gateway_id


class DeleteRequesterGatewayRequest(TypedDict, closed=True):
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRequesterGatewayRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRequesterGatewayRequest:
    out: DeleteRequesterGatewayRequest = {}  # type: ignore[typeddict-item]
    return out
