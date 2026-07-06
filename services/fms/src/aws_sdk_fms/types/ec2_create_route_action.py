"""Generated from Smithy shape ``com.amazonaws.fms#EC2CreateRouteAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.action_target
    import aws_sdk_fms.types.cidr
    import aws_sdk_fms.types.length_bounded_string
    import aws_sdk_fms.types.resource_id


class EC2CreateRouteAction(TypedDict, closed=True):
    description: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>A description of CreateRoute action in Amazon EC2.</p>"""
    destination_cidr_block: NotRequired["aws_sdk_fms.types.cidr.CIDR"]
    """<p>Information about the IPv4 CIDR address block used for the destination match.</p>"""
    destination_prefix_list_id: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>Information about the ID of a prefix list used for the destination match.</p>"""
    destination_ipv6_cidr_block: NotRequired["aws_sdk_fms.types.cidr.CIDR"]
    """<p>Information about the IPv6 CIDR block destination.</p>"""
    vpc_endpoint_id: NotRequired["aws_sdk_fms.types.action_target.ActionTarget"]
    """<p>Information about the ID of a VPC endpoint. Supported for Gateway Load Balancer endpoints only.</p>"""
    gateway_id: NotRequired["aws_sdk_fms.types.action_target.ActionTarget"]
    """<p>Information about the ID of an internet gateway or virtual private gateway attached to your VPC.</p>"""
    route_table_id: "aws_sdk_fms.types.action_target.ActionTarget"
    """<p>Information about the ID of the route table for the route.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2CreateRouteAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "destination_cidr_block" in value:
        out["DestinationCidrBlock"] = value["destination_cidr_block"]
    if "destination_prefix_list_id" in value:
        out["DestinationPrefixListId"] = value["destination_prefix_list_id"]
    if "destination_ipv6_cidr_block" in value:
        out["DestinationIpv6CidrBlock"] = value["destination_ipv6_cidr_block"]
    if "vpc_endpoint_id" in value:
        import aws_sdk_fms.types.action_target

        out["VpcEndpointId"] = aws_sdk_fms.types.action_target.serialize_aws_json_1_1(
            value["vpc_endpoint_id"]
        )
    if "gateway_id" in value:
        import aws_sdk_fms.types.action_target

        out["GatewayId"] = aws_sdk_fms.types.action_target.serialize_aws_json_1_1(
            value["gateway_id"]
        )
    import aws_sdk_fms.types.action_target

    out["RouteTableId"] = aws_sdk_fms.types.action_target.serialize_aws_json_1_1(
        value["route_table_id"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2CreateRouteAction:
    out: EC2CreateRouteAction = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DestinationCidrBlock" in data:
        out["destination_cidr_block"] = data["DestinationCidrBlock"]
    if "DestinationPrefixListId" in data:
        out["destination_prefix_list_id"] = data["DestinationPrefixListId"]
    if "DestinationIpv6CidrBlock" in data:
        out["destination_ipv6_cidr_block"] = data["DestinationIpv6CidrBlock"]
    if "VpcEndpointId" in data:
        import aws_sdk_fms.types.action_target

        out["vpc_endpoint_id"] = (
            aws_sdk_fms.types.action_target.deserialize_aws_json_1_1(
                data["VpcEndpointId"]
            )
        )
    if "GatewayId" in data:
        import aws_sdk_fms.types.action_target

        out["gateway_id"] = aws_sdk_fms.types.action_target.deserialize_aws_json_1_1(
            data["GatewayId"]
        )
    if "RouteTableId" in data:
        import aws_sdk_fms.types.action_target

        out["route_table_id"] = (
            aws_sdk_fms.types.action_target.deserialize_aws_json_1_1(
                data["RouteTableId"]
            )
        )
    else:
        raise DeserializationError("EC2CreateRouteAction.route_table_id required")
    return out
