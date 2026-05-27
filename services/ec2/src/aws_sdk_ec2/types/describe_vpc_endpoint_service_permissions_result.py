"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointServicePermissionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allowed_principal_set
    import aws_sdk_ec2.types.string


class DescribeVpcEndpointServicePermissionsResult(TypedDict):
    allowed_principals: NotRequired[
        "aws_sdk_ec2.types.allowed_principal_set.AllowedPrincipalSet"
    ]
    """<p>Information about the allowed principals.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
