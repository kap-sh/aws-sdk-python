"""Generated from Smithy shape ``com.amazonaws.ec2#AccountAttributeValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.account_attribute_value

AccountAttributeValueList: TypeAlias = list[
    "aws_sdk_ec2.types.account_attribute_value.AccountAttributeValue"
]
