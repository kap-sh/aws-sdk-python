"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Bridge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_bridge_output
    import capo_mediaconnect.types.__list_of_bridge_source
    import capo_mediaconnect.types.__list_of_message_detail
    import capo_mediaconnect.types.bridge_state
    import capo_mediaconnect.types.egress_gateway_bridge
    import capo_mediaconnect.types.failover_config
    import capo_mediaconnect.types.ingress_gateway_bridge


class Bridge(TypedDict, closed=True):
    bridge_arn: NotRequired["str"]
    """<p> The Amazon Resource Number (ARN) of the bridge.</p>"""
    bridge_messages: NotRequired[
        "capo_mediaconnect.types.__list_of_message_detail.__listOfMessageDetail"
    ]
    """<p> Messages with details about the bridge. </p>"""
    bridge_state: NotRequired["capo_mediaconnect.types.bridge_state.BridgeState"]
    """<p>The state of the bridge. </p>"""
    egress_gateway_bridge: NotRequired[
        "capo_mediaconnect.types.egress_gateway_bridge.EgressGatewayBridge"
    ]
    """<p> An egress bridge is a cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises. </p>"""
    ingress_gateway_bridge: NotRequired[
        "capo_mediaconnect.types.ingress_gateway_bridge.IngressGatewayBridge"
    ]
    """<p> An ingress bridge is a ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud. </p>"""
    name: NotRequired["str"]
    """<p> The name of the bridge.</p>"""
    outputs: NotRequired[
        "capo_mediaconnect.types.__list_of_bridge_output.__listOfBridgeOutput"
    ]
    """<p> The outputs on this bridge.</p>"""
    placement_arn: NotRequired["str"]
    """<p> The placement Amazon Resource Number (ARN) of the bridge.</p>"""
    source_failover_config: NotRequired[
        "capo_mediaconnect.types.failover_config.FailoverConfig"
    ]
    """<p> The settings for source failover. </p>"""
    sources: NotRequired[
        "capo_mediaconnect.types.__list_of_bridge_source.__listOfBridgeSource"
    ]
    """<p> The sources on this bridge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Bridge) -> dict:
    out: dict = {}
    if "bridge_arn" in value:
        out["bridgeArn"] = value["bridge_arn"]
    if "bridge_messages" in value:
        import capo_mediaconnect.types.__list_of_message_detail

        out["bridgeMessages"] = (
            capo_mediaconnect.types.__list_of_message_detail.serialize_json(
                value["bridge_messages"]
            )
        )
    if "bridge_state" in value:
        import capo_mediaconnect.types.bridge_state

        out["bridgeState"] = capo_mediaconnect.types.bridge_state.serialize_json(
            value["bridge_state"]
        )
    if "egress_gateway_bridge" in value:
        import capo_mediaconnect.types.egress_gateway_bridge

        out["egressGatewayBridge"] = (
            capo_mediaconnect.types.egress_gateway_bridge.serialize_json(
                value["egress_gateway_bridge"]
            )
        )
    if "ingress_gateway_bridge" in value:
        import capo_mediaconnect.types.ingress_gateway_bridge

        out["ingressGatewayBridge"] = (
            capo_mediaconnect.types.ingress_gateway_bridge.serialize_json(
                value["ingress_gateway_bridge"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "outputs" in value:
        import capo_mediaconnect.types.__list_of_bridge_output

        out["outputs"] = capo_mediaconnect.types.__list_of_bridge_output.serialize_json(
            value["outputs"]
        )
    if "placement_arn" in value:
        out["placementArn"] = value["placement_arn"]
    if "source_failover_config" in value:
        import capo_mediaconnect.types.failover_config

        out["sourceFailoverConfig"] = (
            capo_mediaconnect.types.failover_config.serialize_json(
                value["source_failover_config"]
            )
        )
    if "sources" in value:
        import capo_mediaconnect.types.__list_of_bridge_source

        out["sources"] = capo_mediaconnect.types.__list_of_bridge_source.serialize_json(
            value["sources"]
        )
    return out


def deserialize_json(data: dict) -> Bridge:
    out: Bridge = {}  # type: ignore[typeddict-item]
    if "bridgeArn" in data:
        out["bridge_arn"] = data["bridgeArn"]
    if "bridgeMessages" in data:
        import capo_mediaconnect.types.__list_of_message_detail

        out["bridge_messages"] = (
            capo_mediaconnect.types.__list_of_message_detail.deserialize_json(
                data["bridgeMessages"]
            )
        )
    if "bridgeState" in data:
        import capo_mediaconnect.types.bridge_state

        out["bridge_state"] = capo_mediaconnect.types.bridge_state.deserialize_json(
            data["bridgeState"]
        )
    if "egressGatewayBridge" in data:
        import capo_mediaconnect.types.egress_gateway_bridge

        out["egress_gateway_bridge"] = (
            capo_mediaconnect.types.egress_gateway_bridge.deserialize_json(
                data["egressGatewayBridge"]
            )
        )
    if "ingressGatewayBridge" in data:
        import capo_mediaconnect.types.ingress_gateway_bridge

        out["ingress_gateway_bridge"] = (
            capo_mediaconnect.types.ingress_gateway_bridge.deserialize_json(
                data["ingressGatewayBridge"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "outputs" in data:
        import capo_mediaconnect.types.__list_of_bridge_output

        out["outputs"] = (
            capo_mediaconnect.types.__list_of_bridge_output.deserialize_json(
                data["outputs"]
            )
        )
    if "placementArn" in data:
        out["placement_arn"] = data["placementArn"]
    if "sourceFailoverConfig" in data:
        import capo_mediaconnect.types.failover_config

        out["source_failover_config"] = (
            capo_mediaconnect.types.failover_config.deserialize_json(
                data["sourceFailoverConfig"]
            )
        )
    if "sources" in data:
        import capo_mediaconnect.types.__list_of_bridge_source

        out["sources"] = (
            capo_mediaconnect.types.__list_of_bridge_source.deserialize_json(
                data["sources"]
            )
        )
    return out
