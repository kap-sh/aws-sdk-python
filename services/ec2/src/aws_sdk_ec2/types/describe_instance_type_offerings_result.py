"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceTypeOfferingsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_type_offerings_list
    import aws_sdk_ec2.types.next_token


class DescribeInstanceTypeOfferingsResult(TypedDict):
    instance_type_offerings: NotRequired[
        "aws_sdk_ec2.types.instance_type_offerings_list.InstanceTypeOfferingsList"
    ]
    """<p>The instance types offered in the location.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
