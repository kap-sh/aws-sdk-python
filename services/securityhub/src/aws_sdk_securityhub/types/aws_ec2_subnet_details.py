"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2SubnetDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.ipv6_cidr_block_association_list
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2SubnetDetails(TypedDict):
    assign_ipv6_address_on_creation: NotRequired[
        "aws_sdk_securityhub.types.boolean.Boolean"
    ]
    """<p>Whether to assign an IPV6 address to a network interface that is created in this subnet.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Availability Zone for the subnet.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the Availability Zone for the subnet.</p>"""
    available_ip_address_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of available IPV4 addresses in the subnet. Does not include addresses for stopped instances.</p>"""
    cidr_block: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The IPV4 CIDR block that is assigned to the subnet.</p>"""
    default_for_az: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether this subnet is the default subnet for the Availability Zone.</p>"""
    map_public_ip_on_launch: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether instances in this subnet receive a public IP address.</p>"""
    owner_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the Amazon Web Services account that owns the subnet.</p>"""
    state: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The current state of the subnet. Valid values are <code>available</code> or <code>pending</code>.</p>"""
    subnet_arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the subnet.</p>"""
    subnet_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the subnet.</p>"""
    vpc_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the VPC that contains the subnet.</p>"""
    ipv6_cidr_block_association_set: NotRequired[
        "aws_sdk_securityhub.types.ipv6_cidr_block_association_list.Ipv6CidrBlockAssociationList"
    ]
    """<p>The IPV6 CIDR blocks that are associated with the subnet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2SubnetDetails) -> dict:
    out: dict = {}
    if "assign_ipv6_address_on_creation" in value:
        out["AssignIpv6AddressOnCreation"] = value["assign_ipv6_address_on_creation"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["AvailabilityZoneId"] = value["availability_zone_id"]
    if "available_ip_address_count" in value:
        out["AvailableIpAddressCount"] = value["available_ip_address_count"]
    if "cidr_block" in value:
        out["CidrBlock"] = value["cidr_block"]
    if "default_for_az" in value:
        out["DefaultForAz"] = value["default_for_az"]
    if "map_public_ip_on_launch" in value:
        out["MapPublicIpOnLaunch"] = value["map_public_ip_on_launch"]
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "state" in value:
        out["State"] = value["state"]
    if "subnet_arn" in value:
        out["SubnetArn"] = value["subnet_arn"]
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "ipv6_cidr_block_association_set" in value:
        import aws_sdk_securityhub.types.ipv6_cidr_block_association_list

        out["Ipv6CidrBlockAssociationSet"] = (
            aws_sdk_securityhub.types.ipv6_cidr_block_association_list.serialize_json(
                value["ipv6_cidr_block_association_set"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEc2SubnetDetails:
    out: AwsEc2SubnetDetails = {}  # type: ignore[typeddict-item]
    if "AssignIpv6AddressOnCreation" in data:
        out["assign_ipv6_address_on_creation"] = data["AssignIpv6AddressOnCreation"]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "AvailabilityZoneId" in data:
        out["availability_zone_id"] = data["AvailabilityZoneId"]
    if "AvailableIpAddressCount" in data:
        out["available_ip_address_count"] = data["AvailableIpAddressCount"]
    if "CidrBlock" in data:
        out["cidr_block"] = data["CidrBlock"]
    if "DefaultForAz" in data:
        out["default_for_az"] = data["DefaultForAz"]
    if "MapPublicIpOnLaunch" in data:
        out["map_public_ip_on_launch"] = data["MapPublicIpOnLaunch"]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "State" in data:
        out["state"] = data["State"]
    if "SubnetArn" in data:
        out["subnet_arn"] = data["SubnetArn"]
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "Ipv6CidrBlockAssociationSet" in data:
        import aws_sdk_securityhub.types.ipv6_cidr_block_association_list

        out["ipv6_cidr_block_association_set"] = (
            aws_sdk_securityhub.types.ipv6_cidr_block_association_list.deserialize_json(
                data["Ipv6CidrBlockAssociationSet"]
            )
        )
    return out
