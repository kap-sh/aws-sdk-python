"""Generated from Smithy shape ``com.amazonaws.ec2#BillingProductList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string

BillingProductList: TypeAlias = list["aws_sdk_ec2.types.string.String"]
