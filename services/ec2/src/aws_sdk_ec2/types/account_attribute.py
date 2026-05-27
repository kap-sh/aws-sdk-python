"""Generated from Smithy shape ``com.amazonaws.ec2#AccountAttribute``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.account_attribute_value_list
    import aws_sdk_ec2.types.string


class AccountAttribute(TypedDict):
    attribute_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the account attribute.</p>"""
    attribute_values: NotRequired[
        "aws_sdk_ec2.types.account_attribute_value_list.AccountAttributeValueList"
    ]
    """<p>The values for the account attribute.</p>"""
