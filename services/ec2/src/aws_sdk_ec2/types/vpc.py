"""Generated from Smithy shape ``com.amazonaws.ec2#Vpc``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

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
