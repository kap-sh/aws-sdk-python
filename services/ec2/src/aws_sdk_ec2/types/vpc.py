"""Generated from Smithy shape ``com.amazonaws.ec2#Vpc``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.block_public_access_states
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.tenancy
    import aws_sdk_ec2.types.vpc_cidr_block_association_set
    import aws_sdk_ec2.types.vpc_encryption_control
    import aws_sdk_ec2.types.vpc_ipv6_cidr_block_association_set
    import aws_sdk_ec2.types.vpc_state


class Vpc(TypedDict):
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the VPC.</p>"""
    instance_tenancy: NotRequired["aws_sdk_ec2.types.tenancy.Tenancy"]
    """<p>The allowed tenancy of instances launched into the VPC.</p>"""
    ipv6_cidr_block_association_set: NotRequired[
        "aws_sdk_ec2.types.vpc_ipv6_cidr_block_association_set.VpcIpv6CidrBlockAssociationSet"
    ]
    """<p>Information about the IPv6 CIDR blocks associated with the VPC.</p>"""
    cidr_block_association_set: NotRequired[
        "aws_sdk_ec2.types.vpc_cidr_block_association_set.VpcCidrBlockAssociationSet"
    ]
    """<p>Information about the IPv4 CIDR blocks associated with the VPC.</p>"""
    is_default: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the VPC is the default VPC.</p>"""
    encryption_control: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control.VpcEncryptionControl"
    ]
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the VPC.</p>"""
    block_public_access_states: NotRequired[
        "aws_sdk_ec2.types.block_public_access_states.BlockPublicAccessStates"
    ]
    """<p>The state of VPC Block Public Access (BPA).</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""
    state: NotRequired["aws_sdk_ec2.types.vpc_state.VpcState"]
    """<p>The current state of the VPC.</p>"""
    cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The primary IPv4 CIDR block for the VPC.</p>"""
    dhcp_options_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the set of DHCP options you've associated with the VPC.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(value: Vpc, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "instance_tenancy" in value:
        import aws_sdk_ec2.types.tenancy

        aws_sdk_ec2.types.tenancy.serialize_ec2_query(
            value["instance_tenancy"], pairs, f"{prefix}.InstanceTenancy"
        )
    if "ipv6_cidr_block_association_set" in value:
        import aws_sdk_ec2.types.vpc_ipv6_cidr_block_association_set

        aws_sdk_ec2.types.vpc_ipv6_cidr_block_association_set.serialize_ec2_query(
            value["ipv6_cidr_block_association_set"],
            pairs,
            f"{prefix}.Ipv6CidrBlockAssociationSet",
        )
    if "cidr_block_association_set" in value:
        import aws_sdk_ec2.types.vpc_cidr_block_association_set

        aws_sdk_ec2.types.vpc_cidr_block_association_set.serialize_ec2_query(
            value["cidr_block_association_set"],
            pairs,
            f"{prefix}.CidrBlockAssociationSet",
        )
    if "is_default" in value:
        pairs.append(
            (f"{prefix}.IsDefault", "true" if value["is_default"] else "false")
        )
    if "encryption_control" in value:
        import aws_sdk_ec2.types.vpc_encryption_control

        aws_sdk_ec2.types.vpc_encryption_control.serialize_ec2_query(
            value["encryption_control"], pairs, f"{prefix}.EncryptionControl"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "block_public_access_states" in value:
        import aws_sdk_ec2.types.block_public_access_states

        aws_sdk_ec2.types.block_public_access_states.serialize_ec2_query(
            value["block_public_access_states"],
            pairs,
            f"{prefix}.BlockPublicAccessStates",
        )
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "state" in value:
        import aws_sdk_ec2.types.vpc_state

        aws_sdk_ec2.types.vpc_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "cidr_block" in value:
        pairs.append((f"{prefix}.CidrBlock", str(value["cidr_block"])))
    if "dhcp_options_id" in value:
        pairs.append((f"{prefix}.DhcpOptionsId", str(value["dhcp_options_id"])))


def deserialize_ec2_query(el: Element) -> Vpc:
    out: Vpc = {}  # type: ignore[typeddict-item]
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_instance_tenancy = el.find("InstanceTenancy")
    if child_instance_tenancy is not None:
        import aws_sdk_ec2.types.tenancy

        out["instance_tenancy"] = aws_sdk_ec2.types.tenancy.deserialize_ec2_query(
            child_instance_tenancy
        )
    if el.find("Ipv6CidrBlockAssociationSet") is not None:
        import aws_sdk_ec2.types.vpc_ipv6_cidr_block_association_set

        out["ipv6_cidr_block_association_set"] = (
            aws_sdk_ec2.types.vpc_ipv6_cidr_block_association_set.deserialize_ec2_query(
                el, "Ipv6CidrBlockAssociationSet"
            )
        )
    if el.find("CidrBlockAssociationSet") is not None:
        import aws_sdk_ec2.types.vpc_cidr_block_association_set

        out["cidr_block_association_set"] = (
            aws_sdk_ec2.types.vpc_cidr_block_association_set.deserialize_ec2_query(
                el, "CidrBlockAssociationSet"
            )
        )
    child_is_default = el.find("IsDefault")
    if child_is_default is not None:
        out["is_default"] = (child_is_default.text or "").lower() == "true"
    child_encryption_control = el.find("EncryptionControl")
    if child_encryption_control is not None:
        import aws_sdk_ec2.types.vpc_encryption_control

        out["encryption_control"] = (
            aws_sdk_ec2.types.vpc_encryption_control.deserialize_ec2_query(
                child_encryption_control
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_block_public_access_states = el.find("BlockPublicAccessStates")
    if child_block_public_access_states is not None:
        import aws_sdk_ec2.types.block_public_access_states

        out["block_public_access_states"] = (
            aws_sdk_ec2.types.block_public_access_states.deserialize_ec2_query(
                child_block_public_access_states
            )
        )
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.vpc_state

        out["state"] = aws_sdk_ec2.types.vpc_state.deserialize_ec2_query(child_state)
    child_cidr_block = el.find("CidrBlock")
    if child_cidr_block is not None:
        out["cidr_block"] = str(child_cidr_block.text or "")
    child_dhcp_options_id = el.find("DhcpOptionsId")
    if child_dhcp_options_id is not None:
        out["dhcp_options_id"] = str(child_dhcp_options_id.text or "")
    return out
