"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CreateResponderGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.domain_name
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.listener_config
    import capo_rtbfabric.types.responder_gateway_status


class CreateResponderGatewayResponse(TypedDict, closed=True):
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    status: "capo_rtbfabric.types.responder_gateway_status.ResponderGatewayStatus"
    """<p>The status of the request.</p>"""
    listener_config: NotRequired["capo_rtbfabric.types.listener_config.ListenerConfig"]
    """<p>The listener configuration for the responder gateway.</p>"""
    external_inbound_endpoint: NotRequired[
        "capo_rtbfabric.types.domain_name.DomainName"
    ]
    """<p>The external inbound endpoint for the responder gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResponderGatewayResponse) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    import capo_rtbfabric.types.responder_gateway_status

    out["status"] = capo_rtbfabric.types.responder_gateway_status.serialize_json(
        value["status"]
    )
    if "listener_config" in value:
        import capo_rtbfabric.types.listener_config

        out["listenerConfig"] = capo_rtbfabric.types.listener_config.serialize_json(
            value["listener_config"]
        )
    if "external_inbound_endpoint" in value:
        out["externalInboundEndpoint"] = value["external_inbound_endpoint"]
    return out


def deserialize_json(data: dict) -> CreateResponderGatewayResponse:
    out: CreateResponderGatewayResponse = {}  # type: ignore[typeddict-item]
    if "gatewayId" in data:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("CreateResponderGatewayResponse.gateway_id required")
    if "status" in data:
        import capo_rtbfabric.types.responder_gateway_status

        out["status"] = capo_rtbfabric.types.responder_gateway_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreateResponderGatewayResponse.status required")
    if "listenerConfig" in data:
        import capo_rtbfabric.types.listener_config

        out["listener_config"] = capo_rtbfabric.types.listener_config.deserialize_json(
            data["listenerConfig"]
        )
    if "externalInboundEndpoint" in data:
        out["external_inbound_endpoint"] = data["externalInboundEndpoint"]
    return out
