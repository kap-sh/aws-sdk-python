"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.purchase

PurchaseSet: TypeAlias = list["aws_sdk_ec2.types.purchase.Purchase"]
