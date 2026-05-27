"""Generated from Smithy shape ``com.amazonaws.ec2#SuccessfulQueuedPurchaseDeletionSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.successful_queued_purchase_deletion

SuccessfulQueuedPurchaseDeletionSet: TypeAlias = list[
    "aws_sdk_ec2.types.successful_queued_purchase_deletion.SuccessfulQueuedPurchaseDeletion"
]
