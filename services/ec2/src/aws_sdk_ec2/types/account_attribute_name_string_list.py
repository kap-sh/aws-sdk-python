"""Generated from Smithy shape ``com.amazonaws.ec2#AccountAttributeNameStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.account_attribute_name

AccountAttributeNameStringList: TypeAlias = list[
    "aws_sdk_ec2.types.account_attribute_name.AccountAttributeName"
]
