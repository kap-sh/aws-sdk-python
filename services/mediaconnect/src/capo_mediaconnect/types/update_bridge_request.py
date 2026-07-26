"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateBridgeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.bridge_arn
    import capo_mediaconnect.types.update_egress_gateway_bridge_request
    import capo_mediaconnect.types.update_failover_config
    import capo_mediaconnect.types.update_ingress_gateway_bridge_request


class UpdateBridgeRequest(TypedDict, closed=True):
    bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn"
    """<p> TheAmazon Resource Name (ARN) of the bridge that you want to update. </p>"""
    egress_gateway_bridge: NotRequired[
        "capo_mediaconnect.types.update_egress_gateway_bridge_request.UpdateEgressGatewayBridgeRequest"
    ]
    """<p> A cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises. </p>"""
    ingress_gateway_bridge: NotRequired[
        "capo_mediaconnect.types.update_ingress_gateway_bridge_request.UpdateIngressGatewayBridgeRequest"
    ]
    """<p> A ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud. </p>"""
    source_failover_config: NotRequired[
        "capo_mediaconnect.types.update_failover_config.UpdateFailoverConfig"
    ]
    """<p> The settings for source failover. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBridgeRequest) -> dict:
    out: dict = {}
    if "egress_gateway_bridge" in value:
        import capo_mediaconnect.types.update_egress_gateway_bridge_request

        out["egressGatewayBridge"] = (
            capo_mediaconnect.types.update_egress_gateway_bridge_request.serialize_json(
                value["egress_gateway_bridge"]
            )
        )
    if "ingress_gateway_bridge" in value:
        import capo_mediaconnect.types.update_ingress_gateway_bridge_request

        out["ingressGatewayBridge"] = (
            capo_mediaconnect.types.update_ingress_gateway_bridge_request.serialize_json(
                value["ingress_gateway_bridge"]
            )
        )
    if "source_failover_config" in value:
        import capo_mediaconnect.types.update_failover_config

        out["sourceFailoverConfig"] = (
            capo_mediaconnect.types.update_failover_config.serialize_json(
                value["source_failover_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBridgeRequest:
    out: UpdateBridgeRequest = {}  # type: ignore[typeddict-item]
    if "egressGatewayBridge" in data:
        import capo_mediaconnect.types.update_egress_gateway_bridge_request

        out["egress_gateway_bridge"] = (
            capo_mediaconnect.types.update_egress_gateway_bridge_request.deserialize_json(
                data["egressGatewayBridge"]
            )
        )
    if "ingressGatewayBridge" in data:
        import capo_mediaconnect.types.update_ingress_gateway_bridge_request

        out["ingress_gateway_bridge"] = (
            capo_mediaconnect.types.update_ingress_gateway_bridge_request.deserialize_json(
                data["ingressGatewayBridge"]
            )
        )
    if "sourceFailoverConfig" in data:
        import capo_mediaconnect.types.update_failover_config

        out["source_failover_config"] = (
            capo_mediaconnect.types.update_failover_config.deserialize_json(
                data["sourceFailoverConfig"]
            )
        )
    return out
