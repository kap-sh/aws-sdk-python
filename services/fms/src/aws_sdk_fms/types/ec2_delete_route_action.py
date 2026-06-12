"""Generated from Smithy shape ``com.amazonaws.fms#EC2DeleteRouteAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.action_target
    import aws_sdk_fms.types.cidr
    import aws_sdk_fms.types.length_bounded_string
    import aws_sdk_fms.types.resource_id


class EC2DeleteRouteAction(TypedDict):
    description: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>A description of the DeleteRoute action.</p>"""
    destination_cidr_block: NotRequired["aws_sdk_fms.types.cidr.CIDR"]
    """<p>Information about the IPv4 CIDR range for the route. The value you specify must match the CIDR for the route exactly.</p>"""
    destination_prefix_list_id: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>Information about the ID of the prefix list for the route.</p>"""
    destination_ipv6_cidr_block: NotRequired["aws_sdk_fms.types.cidr.CIDR"]
    """<p>Information about the IPv6 CIDR range for the route. The value you specify must match the CIDR for the route exactly.</p>"""
    route_table_id: "aws_sdk_fms.types.action_target.ActionTarget"
    """<p>Information about the ID of the route table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2DeleteRouteAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "destination_cidr_block" in value:
        out["DestinationCidrBlock"] = value["destination_cidr_block"]
    if "destination_prefix_list_id" in value:
        out["DestinationPrefixListId"] = value["destination_prefix_list_id"]
    if "destination_ipv6_cidr_block" in value:
        out["DestinationIpv6CidrBlock"] = value["destination_ipv6_cidr_block"]
    import aws_sdk_fms.types.action_target

    out["RouteTableId"] = aws_sdk_fms.types.action_target.serialize_aws_json_1_1(
        value["route_table_id"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2DeleteRouteAction:
    out: EC2DeleteRouteAction = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DestinationCidrBlock" in data:
        out["destination_cidr_block"] = data["DestinationCidrBlock"]
    if "DestinationPrefixListId" in data:
        out["destination_prefix_list_id"] = data["DestinationPrefixListId"]
    if "DestinationIpv6CidrBlock" in data:
        out["destination_ipv6_cidr_block"] = data["DestinationIpv6CidrBlock"]
    if "RouteTableId" in data:
        import aws_sdk_fms.types.action_target

        out["route_table_id"] = (
            aws_sdk_fms.types.action_target.deserialize_aws_json_1_1(
                data["RouteTableId"]
            )
        )
    else:
        raise DeserializationError("EC2DeleteRouteAction.route_table_id required")
    return out
