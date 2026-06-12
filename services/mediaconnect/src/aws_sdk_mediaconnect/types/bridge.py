"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Bridge``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_bridge_output
    import aws_sdk_mediaconnect.types.__list_of_bridge_source
    import aws_sdk_mediaconnect.types.__list_of_message_detail
    import aws_sdk_mediaconnect.types.bridge_state
    import aws_sdk_mediaconnect.types.egress_gateway_bridge
    import aws_sdk_mediaconnect.types.failover_config
    import aws_sdk_mediaconnect.types.ingress_gateway_bridge

class Bridge(TypedDict):
    bridge_arn: NotRequired["str"]
    """<p> The Amazon Resource Number (ARN) of the bridge.</p>"""
    bridge_messages: NotRequired["aws_sdk_mediaconnect.types.__list_of_message_detail.__listOfMessageDetail"]
    """<p> Messages with details about the bridge. </p>"""
    bridge_state: NotRequired["aws_sdk_mediaconnect.types.bridge_state.BridgeState"]
    """<p>The state of the bridge. </p>"""
    egress_gateway_bridge: NotRequired["aws_sdk_mediaconnect.types.egress_gateway_bridge.EgressGatewayBridge"]
    """<p> An egress bridge is a cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises. </p>"""
    ingress_gateway_bridge: NotRequired["aws_sdk_mediaconnect.types.ingress_gateway_bridge.IngressGatewayBridge"]
    """<p> An ingress bridge is a ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud. </p>"""
    name: NotRequired["str"]
    """<p> The name of the bridge.</p>"""
    outputs: NotRequired["aws_sdk_mediaconnect.types.__list_of_bridge_output.__listOfBridgeOutput"]
    """<p> The outputs on this bridge.</p>"""
    placement_arn: NotRequired["str"]
    """<p> The placement Amazon Resource Number (ARN) of the bridge.</p>"""
    source_failover_config: NotRequired["aws_sdk_mediaconnect.types.failover_config.FailoverConfig"]
    """<p> The settings for source failover. </p>"""
    sources: NotRequired["aws_sdk_mediaconnect.types.__list_of_bridge_source.__listOfBridgeSource"]
    """<p> The sources on this bridge.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: Bridge) -> dict:
    out: dict = {}
    if "bridge_arn" in value:
        out["bridgeArn"] = value["bridge_arn"]
    if "bridge_messages" in value:
        import aws_sdk_mediaconnect.types.__list_of_message_detail
        out["bridgeMessages"] = aws_sdk_mediaconnect.types.__list_of_message_detail.serialize_json(value["bridge_messages"])
    if "bridge_state" in value:
        import aws_sdk_mediaconnect.types.bridge_state
        out["bridgeState"] = aws_sdk_mediaconnect.types.bridge_state.serialize_json(value["bridge_state"])
    if "egress_gateway_bridge" in value:
        import aws_sdk_mediaconnect.types.egress_gateway_bridge
        out["egressGatewayBridge"] = aws_sdk_mediaconnect.types.egress_gateway_bridge.serialize_json(value["egress_gateway_bridge"])
    if "ingress_gateway_bridge" in value:
        import aws_sdk_mediaconnect.types.ingress_gateway_bridge
        out["ingressGatewayBridge"] = aws_sdk_mediaconnect.types.ingress_gateway_bridge.serialize_json(value["ingress_gateway_bridge"])
    if "name" in value:
        out["name"] = value["name"]
    if "outputs" in value:
        import aws_sdk_mediaconnect.types.__list_of_bridge_output
        out["outputs"] = aws_sdk_mediaconnect.types.__list_of_bridge_output.serialize_json(value["outputs"])
    if "placement_arn" in value:
        out["placementArn"] = value["placement_arn"]
    if "source_failover_config" in value:
        import aws_sdk_mediaconnect.types.failover_config
        out["sourceFailoverConfig"] = aws_sdk_mediaconnect.types.failover_config.serialize_json(value["source_failover_config"])
    if "sources" in value:
        import aws_sdk_mediaconnect.types.__list_of_bridge_source
        out["sources"] = aws_sdk_mediaconnect.types.__list_of_bridge_source.serialize_json(value["sources"])
    return out


def deserialize_json(data: dict) -> Bridge:
    out: Bridge = {}  # type: ignore[typeddict-item]
    if "bridgeArn" in data:
        out["bridge_arn"] = data["bridgeArn"]
    if "bridgeMessages" in data:
        import aws_sdk_mediaconnect.types.__list_of_message_detail
        out["bridge_messages"] = aws_sdk_mediaconnect.types.__list_of_message_detail.deserialize_json(data["bridgeMessages"])
    if "bridgeState" in data:
        import aws_sdk_mediaconnect.types.bridge_state
        out["bridge_state"] = aws_sdk_mediaconnect.types.bridge_state.deserialize_json(data["bridgeState"])
    if "egressGatewayBridge" in data:
        import aws_sdk_mediaconnect.types.egress_gateway_bridge
        out["egress_gateway_bridge"] = aws_sdk_mediaconnect.types.egress_gateway_bridge.deserialize_json(data["egressGatewayBridge"])
    if "ingressGatewayBridge" in data:
        import aws_sdk_mediaconnect.types.ingress_gateway_bridge
        out["ingress_gateway_bridge"] = aws_sdk_mediaconnect.types.ingress_gateway_bridge.deserialize_json(data["ingressGatewayBridge"])
    if "name" in data:
        out["name"] = data["name"]
    if "outputs" in data:
        import aws_sdk_mediaconnect.types.__list_of_bridge_output
        out["outputs"] = aws_sdk_mediaconnect.types.__list_of_bridge_output.deserialize_json(data["outputs"])
    if "placementArn" in data:
        out["placement_arn"] = data["placementArn"]
    if "sourceFailoverConfig" in data:
        import aws_sdk_mediaconnect.types.failover_config
        out["source_failover_config"] = aws_sdk_mediaconnect.types.failover_config.deserialize_json(data["sourceFailoverConfig"])
    if "sources" in data:
        import aws_sdk_mediaconnect.types.__list_of_bridge_source
        out["sources"] = aws_sdk_mediaconnect.types.__list_of_bridge_source.deserialize_json(data["sources"])
    return out