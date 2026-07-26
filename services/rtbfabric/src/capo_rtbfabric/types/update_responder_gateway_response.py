"""Generated from Smithy shape ``com.amazonaws.rtbfabric#UpdateResponderGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.responder_gateway_status


class UpdateResponderGatewayResponse(TypedDict, closed=True):
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    status: "capo_rtbfabric.types.responder_gateway_status.ResponderGatewayStatus"
    """<p>The status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResponderGatewayResponse) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    import capo_rtbfabric.types.responder_gateway_status

    out["status"] = capo_rtbfabric.types.responder_gateway_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateResponderGatewayResponse:
    out: UpdateResponderGatewayResponse = {}  # type: ignore[typeddict-item]
    if "gatewayId" in data:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("UpdateResponderGatewayResponse.gateway_id required")
    if "status" in data:
        import capo_rtbfabric.types.responder_gateway_status

        out["status"] = capo_rtbfabric.types.responder_gateway_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateResponderGatewayResponse.status required")
    return out
