"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAccountAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.account_attribute_name_string_list
    import aws_sdk_ec2.types.boolean


class DescribeAccountAttributesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    attribute_names: NotRequired[
        "aws_sdk_ec2.types.account_attribute_name_string_list.AccountAttributeNameStringList"
    ]
    """<p>The account attribute names.</p>"""
