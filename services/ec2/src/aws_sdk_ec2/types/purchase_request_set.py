"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseRequestSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.purchase_request

PurchaseRequestSet: TypeAlias = list[
    "aws_sdk_ec2.types.purchase_request.PurchaseRequest"
]
