"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSpotInstanceRequestsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.spot_instance_request_list
    import aws_sdk_ec2.types.string


class DescribeSpotInstanceRequestsResult(TypedDict):
    spot_instance_requests: NotRequired[
        "aws_sdk_ec2.types.spot_instance_request_list.SpotInstanceRequestList"
    ]
    """<p>The Spot Instance requests.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
