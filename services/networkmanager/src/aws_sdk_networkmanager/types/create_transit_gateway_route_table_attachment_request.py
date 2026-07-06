"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateTransitGatewayRouteTableAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.client_token
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.peering_id
    import aws_sdk_networkmanager.types.tag_list
    import aws_sdk_networkmanager.types.transit_gateway_route_table_arn


class CreateTransitGatewayRouteTableAttachmentRequest(TypedDict, closed=True):
    peering_id: "aws_sdk_networkmanager.types.peering_id.PeeringId"
    """<p>The ID of the peer for the </p>"""
    transit_gateway_route_table_arn: "aws_sdk_networkmanager.types.transit_gateway_route_table_arn.TransitGatewayRouteTableArn"
    r"""<p>The ARN of the transit gateway route table for the attachment request. For example, <code>\"TransitGatewayRouteTableArn\": \"arn:aws:ec2:us-west-2:123456789012:transit-gateway-route-table/tgw-rtb-9876543210123456\"</code>.</p>"""
    routing_policy_label: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The routing policy label to apply to the Transit Gateway route table attachment for traffic routing decisions.</p>"""
    tags: NotRequired["aws_sdk_networkmanager.types.tag_list.TagList"]
    """<p>The list of key-value tags associated with the request.</p>"""
    client_token: NotRequired["aws_sdk_networkmanager.types.client_token.ClientToken"]
    """<p>The client token associated with the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTransitGatewayRouteTableAttachmentRequest) -> dict:
    out: dict = {}
    out["PeeringId"] = value["peering_id"]
    out["TransitGatewayRouteTableArn"] = value["transit_gateway_route_table_arn"]
    if "routing_policy_label" in value:
        out["RoutingPolicyLabel"] = value["routing_policy_label"]
    if "tags" in value:
        import aws_sdk_networkmanager.types.tag_list

        out["Tags"] = aws_sdk_networkmanager.types.tag_list.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateTransitGatewayRouteTableAttachmentRequest:
    out: CreateTransitGatewayRouteTableAttachmentRequest = {}  # type: ignore[typeddict-item]
    if "PeeringId" in data:
        out["peering_id"] = data["PeeringId"]
    else:
        raise DeserializationError(
            "CreateTransitGatewayRouteTableAttachmentRequest.peering_id required"
        )
    if "TransitGatewayRouteTableArn" in data:
        out["transit_gateway_route_table_arn"] = data["TransitGatewayRouteTableArn"]
    else:
        raise DeserializationError(
            "CreateTransitGatewayRouteTableAttachmentRequest.transit_gateway_route_table_arn required"
        )
    if "RoutingPolicyLabel" in data:
        out["routing_policy_label"] = data["RoutingPolicyLabel"]
    if "Tags" in data:
        import aws_sdk_networkmanager.types.tag_list

        out["tags"] = aws_sdk_networkmanager.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
