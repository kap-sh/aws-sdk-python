"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupReference``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class SecurityGroupReference(TypedDict):
    group_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of your security group.</p>"""
    referencing_vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC with the referencing security group.</p>"""
    vpc_peering_connection_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC peering connection (if applicable). For more information about security group referencing for peering connections, see <a href=\"https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-security-groups.html\">Update your security groups to reference peer security groups</a> in the <i>VPC Peering Guide</i>.</p>"""
    transit_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway (if applicable).</p>"""
