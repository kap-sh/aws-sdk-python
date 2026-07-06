"""Generated from Smithy shape ``com.amazonaws.mediaconnect#CreateBridgeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_add_bridge_output_request
    import aws_sdk_mediaconnect.types.__list_of_add_bridge_source_request
    import aws_sdk_mediaconnect.types.add_egress_gateway_bridge_request
    import aws_sdk_mediaconnect.types.add_ingress_gateway_bridge_request
    import aws_sdk_mediaconnect.types.failover_config


class CreateBridgeRequest(TypedDict, closed=True):
    egress_gateway_bridge: NotRequired[
        "aws_sdk_mediaconnect.types.add_egress_gateway_bridge_request.AddEgressGatewayBridgeRequest"
    ]
    """<p>An egress bridge is a cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises. </p>"""
    ingress_gateway_bridge: NotRequired[
        "aws_sdk_mediaconnect.types.add_ingress_gateway_bridge_request.AddIngressGatewayBridgeRequest"
    ]
    """<p>An ingress bridge is a ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud. </p>"""
    name: NotRequired["str"]
    """<p> The name of the bridge. This name can not be modified after the bridge is created.</p>"""
    outputs: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_add_bridge_output_request.__listOfAddBridgeOutputRequest"
    ]
    """<p> The outputs that you want to add to this bridge.</p>"""
    placement_arn: NotRequired["str"]
    """<p> The bridge placement Amazon Resource Number (ARN).</p>"""
    source_failover_config: NotRequired[
        "aws_sdk_mediaconnect.types.failover_config.FailoverConfig"
    ]
    """<p> The settings for source failover.</p>"""
    sources: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_add_bridge_source_request.__listOfAddBridgeSourceRequest"
    ]
    """<p> The sources that you want to add to this bridge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBridgeRequest) -> dict:
    out: dict = {}
    if "egress_gateway_bridge" in value:
        import aws_sdk_mediaconnect.types.add_egress_gateway_bridge_request

        out["egressGatewayBridge"] = (
            aws_sdk_mediaconnect.types.add_egress_gateway_bridge_request.serialize_json(
                value["egress_gateway_bridge"]
            )
        )
    if "ingress_gateway_bridge" in value:
        import aws_sdk_mediaconnect.types.add_ingress_gateway_bridge_request

        out["ingressGatewayBridge"] = (
            aws_sdk_mediaconnect.types.add_ingress_gateway_bridge_request.serialize_json(
                value["ingress_gateway_bridge"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "outputs" in value:
        import aws_sdk_mediaconnect.types.__list_of_add_bridge_output_request

        out["outputs"] = (
            aws_sdk_mediaconnect.types.__list_of_add_bridge_output_request.serialize_json(
                value["outputs"]
            )
        )
    if "placement_arn" in value:
        out["placementArn"] = value["placement_arn"]
    if "source_failover_config" in value:
        import aws_sdk_mediaconnect.types.failover_config

        out["sourceFailoverConfig"] = (
            aws_sdk_mediaconnect.types.failover_config.serialize_json(
                value["source_failover_config"]
            )
        )
    if "sources" in value:
        import aws_sdk_mediaconnect.types.__list_of_add_bridge_source_request

        out["sources"] = (
            aws_sdk_mediaconnect.types.__list_of_add_bridge_source_request.serialize_json(
                value["sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateBridgeRequest:
    out: CreateBridgeRequest = {}  # type: ignore[typeddict-item]
    if "egressGatewayBridge" in data:
        import aws_sdk_mediaconnect.types.add_egress_gateway_bridge_request

        out["egress_gateway_bridge"] = (
            aws_sdk_mediaconnect.types.add_egress_gateway_bridge_request.deserialize_json(
                data["egressGatewayBridge"]
            )
        )
    if "ingressGatewayBridge" in data:
        import aws_sdk_mediaconnect.types.add_ingress_gateway_bridge_request

        out["ingress_gateway_bridge"] = (
            aws_sdk_mediaconnect.types.add_ingress_gateway_bridge_request.deserialize_json(
                data["ingressGatewayBridge"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "outputs" in data:
        import aws_sdk_mediaconnect.types.__list_of_add_bridge_output_request

        out["outputs"] = (
            aws_sdk_mediaconnect.types.__list_of_add_bridge_output_request.deserialize_json(
                data["outputs"]
            )
        )
    if "placementArn" in data:
        out["placement_arn"] = data["placementArn"]
    if "sourceFailoverConfig" in data:
        import aws_sdk_mediaconnect.types.failover_config

        out["source_failover_config"] = (
            aws_sdk_mediaconnect.types.failover_config.deserialize_json(
                data["sourceFailoverConfig"]
            )
        )
    if "sources" in data:
        import aws_sdk_mediaconnect.types.__list_of_add_bridge_source_request

        out["sources"] = (
            aws_sdk_mediaconnect.types.__list_of_add_bridge_source_request.deserialize_json(
                data["sources"]
            )
        )
    return out
