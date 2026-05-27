"""Generated from Smithy shape ``com.amazonaws.ec2#AccountAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.account_attribute

AccountAttributeList: TypeAlias = list[
    "aws_sdk_ec2.types.account_attribute.AccountAttribute"
]
