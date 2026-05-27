"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecurityGroupVpcAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_vpc_association_list
    import aws_sdk_ec2.types.string


class DescribeSecurityGroupVpcAssociationsResult(TypedDict):
    security_group_vpc_associations: NotRequired[
        "aws_sdk_ec2.types.security_group_vpc_association_list.SecurityGroupVpcAssociationList"
    ]
    """<p>The security group VPC associations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
