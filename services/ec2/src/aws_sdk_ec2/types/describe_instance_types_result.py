"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceTypesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_type_info_list
    import aws_sdk_ec2.types.next_token


class DescribeInstanceTypesResult(TypedDict):
    instance_types: NotRequired[
        "aws_sdk_ec2.types.instance_type_info_list.InstanceTypeInfoList"
    ]
    """<p>The instance type.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
