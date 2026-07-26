"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2VpcDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.cidr_block_association_list
    import capo_securityhub.types.ipv6_cidr_block_association_list
    import capo_securityhub.types.non_empty_string


class AwsEc2VpcDetails(TypedDict, closed=True):
    cidr_block_association_set: NotRequired[
        "capo_securityhub.types.cidr_block_association_list.CidrBlockAssociationList"
    ]
    """<p>Information about the IPv4 CIDR blocks associated with the VPC.</p>"""
    ipv6_cidr_block_association_set: NotRequired[
        "capo_securityhub.types.ipv6_cidr_block_association_list.Ipv6CidrBlockAssociationList"
    ]
    """<p>Information about the IPv6 CIDR blocks associated with the VPC.</p>"""
    dhcp_options_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the set of Dynamic Host Configuration Protocol (DHCP) options that are associated with the VPC. If the default options are associated with the VPC, then this is default.</p>"""
    state: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The current state of the VPC. Valid values are <code>available</code> or <code>pending</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2VpcDetails) -> dict:
    out: dict = {}
    if "cidr_block_association_set" in value:
        import capo_securityhub.types.cidr_block_association_list

        out["CidrBlockAssociationSet"] = (
            capo_securityhub.types.cidr_block_association_list.serialize_json(
                value["cidr_block_association_set"]
            )
        )
    if "ipv6_cidr_block_association_set" in value:
        import capo_securityhub.types.ipv6_cidr_block_association_list

        out["Ipv6CidrBlockAssociationSet"] = (
            capo_securityhub.types.ipv6_cidr_block_association_list.serialize_json(
                value["ipv6_cidr_block_association_set"]
            )
        )
    if "dhcp_options_id" in value:
        out["DhcpOptionsId"] = value["dhcp_options_id"]
    if "state" in value:
        out["State"] = value["state"]
    return out


def deserialize_json(data: dict) -> AwsEc2VpcDetails:
    out: AwsEc2VpcDetails = {}  # type: ignore[typeddict-item]
    if "CidrBlockAssociationSet" in data:
        import capo_securityhub.types.cidr_block_association_list

        out["cidr_block_association_set"] = (
            capo_securityhub.types.cidr_block_association_list.deserialize_json(
                data["CidrBlockAssociationSet"]
            )
        )
    if "Ipv6CidrBlockAssociationSet" in data:
        import capo_securityhub.types.ipv6_cidr_block_association_list

        out["ipv6_cidr_block_association_set"] = (
            capo_securityhub.types.ipv6_cidr_block_association_list.deserialize_json(
                data["Ipv6CidrBlockAssociationSet"]
            )
        )
    if "DhcpOptionsId" in data:
        out["dhcp_options_id"] = data["DhcpOptionsId"]
    if "State" in data:
        out["state"] = data["State"]
    return out
