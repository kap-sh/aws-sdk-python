"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAccountAttributesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.account_attribute_list


class DescribeAccountAttributesResult(TypedDict):
    account_attributes: NotRequired[
        "aws_sdk_ec2.types.account_attribute_list.AccountAttributeList"
    ]
    """<p>Information about the account attributes.</p>"""
