"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceCreditSpecificationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_credit_specification_list
    import aws_sdk_ec2.types.string


class DescribeInstanceCreditSpecificationsResult(TypedDict):
    instance_credit_specifications: NotRequired[
        "aws_sdk_ec2.types.instance_credit_specification_list.InstanceCreditSpecificationList"
    ]
    """<p>Information about the credit option for CPU usage of an instance.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
