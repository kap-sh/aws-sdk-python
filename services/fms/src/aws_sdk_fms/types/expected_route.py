"""Generated from Smithy shape ``com.amazonaws.fms#ExpectedRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fms.types.cidr
    import aws_sdk_fms.types.length_bounded_string_list
    import aws_sdk_fms.types.resource_id
    import aws_sdk_fms.types.resource_id_list


class ExpectedRoute(TypedDict, closed=True):
    ip_v4_cidr: NotRequired["aws_sdk_fms.types.cidr.CIDR"]
    """<p>Information about the IPv4 CIDR block.</p>"""
    prefix_list_id: NotRequired["aws_sdk_fms.types.cidr.CIDR"]
    """<p>Information about the ID of the prefix list for the route.</p>"""
    ip_v6_cidr: NotRequired["aws_sdk_fms.types.cidr.CIDR"]
    """<p>Information about the IPv6 CIDR block.</p>"""
    contributing_subnets: NotRequired[
        "aws_sdk_fms.types.resource_id_list.ResourceIdList"
    ]
    """<p>Information about the contributing subnets.</p>"""
    allowed_targets: NotRequired[
        "aws_sdk_fms.types.length_bounded_string_list.LengthBoundedStringList"
    ]
    """<p>Information about the allowed targets.</p>"""
    route_table_id: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>Information about the route table ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpectedRoute) -> dict:
    out: dict = {}
    if "ip_v4_cidr" in value:
        out["IpV4Cidr"] = value["ip_v4_cidr"]
    if "prefix_list_id" in value:
        out["PrefixListId"] = value["prefix_list_id"]
    if "ip_v6_cidr" in value:
        out["IpV6Cidr"] = value["ip_v6_cidr"]
    if "contributing_subnets" in value:
        import aws_sdk_fms.types.resource_id_list

        out["ContributingSubnets"] = (
            aws_sdk_fms.types.resource_id_list.serialize_aws_json_1_1(
                value["contributing_subnets"]
            )
        )
    if "allowed_targets" in value:
        import aws_sdk_fms.types.length_bounded_string_list

        out["AllowedTargets"] = (
            aws_sdk_fms.types.length_bounded_string_list.serialize_aws_json_1_1(
                value["allowed_targets"]
            )
        )
    if "route_table_id" in value:
        out["RouteTableId"] = value["route_table_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpectedRoute:
    out: ExpectedRoute = {}  # type: ignore[typeddict-item]
    if "IpV4Cidr" in data:
        out["ip_v4_cidr"] = data["IpV4Cidr"]
    if "PrefixListId" in data:
        out["prefix_list_id"] = data["PrefixListId"]
    if "IpV6Cidr" in data:
        out["ip_v6_cidr"] = data["IpV6Cidr"]
    if "ContributingSubnets" in data:
        import aws_sdk_fms.types.resource_id_list

        out["contributing_subnets"] = (
            aws_sdk_fms.types.resource_id_list.deserialize_aws_json_1_1(
                data["ContributingSubnets"]
            )
        )
    if "AllowedTargets" in data:
        import aws_sdk_fms.types.length_bounded_string_list

        out["allowed_targets"] = (
            aws_sdk_fms.types.length_bounded_string_list.deserialize_aws_json_1_1(
                data["AllowedTargets"]
            )
        )
    if "RouteTableId" in data:
        out["route_table_id"] = data["RouteTableId"]
    return out
