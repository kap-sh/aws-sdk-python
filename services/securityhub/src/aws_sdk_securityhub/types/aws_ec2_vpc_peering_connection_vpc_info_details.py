"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2VpcPeeringConnectionVpcInfoDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.vpc_info_cidr_block_set_list
    import aws_sdk_securityhub.types.vpc_info_ipv6_cidr_block_set_list
    import aws_sdk_securityhub.types.vpc_info_peering_options_details


class AwsEc2VpcPeeringConnectionVpcInfoDetails(TypedDict):
    cidr_block: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The IPv4 CIDR block for the VPC. </p>"""
    cidr_block_set: NotRequired[
        "aws_sdk_securityhub.types.vpc_info_cidr_block_set_list.VpcInfoCidrBlockSetList"
    ]
    """<p>Information about the IPv4 CIDR blocks for the VPC. </p>"""
    ipv6_cidr_block_set: NotRequired[
        "aws_sdk_securityhub.types.vpc_info_ipv6_cidr_block_set_list.VpcInfoIpv6CidrBlockSetList"
    ]
    """<p>The IPv6 CIDR block for the VPC. </p>"""
    owner_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the Amazon Web Services account that owns the VPC. </p>"""
    peering_options: NotRequired[
        "aws_sdk_securityhub.types.vpc_info_peering_options_details.VpcInfoPeeringOptionsDetails"
    ]
    """<p>Information about the VPC peering connection options for the accepter or requester VPC. </p>"""
    region: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services Region in which the VPC is located. </p>"""
    vpc_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the VPC. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2VpcPeeringConnectionVpcInfoDetails) -> dict:
    out: dict = {}
    if "cidr_block" in value:
        out["CidrBlock"] = value["cidr_block"]
    if "cidr_block_set" in value:
        import aws_sdk_securityhub.types.vpc_info_cidr_block_set_list

        out["CidrBlockSet"] = (
            aws_sdk_securityhub.types.vpc_info_cidr_block_set_list.serialize_json(
                value["cidr_block_set"]
            )
        )
    if "ipv6_cidr_block_set" in value:
        import aws_sdk_securityhub.types.vpc_info_ipv6_cidr_block_set_list

        out["Ipv6CidrBlockSet"] = (
            aws_sdk_securityhub.types.vpc_info_ipv6_cidr_block_set_list.serialize_json(
                value["ipv6_cidr_block_set"]
            )
        )
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "peering_options" in value:
        import aws_sdk_securityhub.types.vpc_info_peering_options_details

        out["PeeringOptions"] = (
            aws_sdk_securityhub.types.vpc_info_peering_options_details.serialize_json(
                value["peering_options"]
            )
        )
    if "region" in value:
        out["Region"] = value["region"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> AwsEc2VpcPeeringConnectionVpcInfoDetails:
    out: AwsEc2VpcPeeringConnectionVpcInfoDetails = {}  # type: ignore[typeddict-item]
    if "CidrBlock" in data:
        out["cidr_block"] = data["CidrBlock"]
    if "CidrBlockSet" in data:
        import aws_sdk_securityhub.types.vpc_info_cidr_block_set_list

        out["cidr_block_set"] = (
            aws_sdk_securityhub.types.vpc_info_cidr_block_set_list.deserialize_json(
                data["CidrBlockSet"]
            )
        )
    if "Ipv6CidrBlockSet" in data:
        import aws_sdk_securityhub.types.vpc_info_ipv6_cidr_block_set_list

        out["ipv6_cidr_block_set"] = (
            aws_sdk_securityhub.types.vpc_info_ipv6_cidr_block_set_list.deserialize_json(
                data["Ipv6CidrBlockSet"]
            )
        )
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "PeeringOptions" in data:
        import aws_sdk_securityhub.types.vpc_info_peering_options_details

        out["peering_options"] = (
            aws_sdk_securityhub.types.vpc_info_peering_options_details.deserialize_json(
                data["PeeringOptions"]
            )
        )
    if "Region" in data:
        out["region"] = data["Region"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    return out
