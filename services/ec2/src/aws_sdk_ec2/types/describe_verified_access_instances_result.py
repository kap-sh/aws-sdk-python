"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVerifiedAccessInstancesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.verified_access_instance_list


class DescribeVerifiedAccessInstancesResult(TypedDict):
    verified_access_instances: NotRequired[
        "aws_sdk_ec2.types.verified_access_instance_list.VerifiedAccessInstanceList"
    ]
    """<p>Details about the Verified Access instances.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
