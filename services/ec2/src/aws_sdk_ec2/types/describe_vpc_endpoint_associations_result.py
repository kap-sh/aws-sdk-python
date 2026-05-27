"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_endpoint_association_set


class DescribeVpcEndpointAssociationsResult(TypedDict):
    vpc_endpoint_associations: NotRequired[
        "aws_sdk_ec2.types.vpc_endpoint_association_set.VpcEndpointAssociationSet"
    ]
    """<p>Details of the endpoint associations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The pagination token.</p>"""
