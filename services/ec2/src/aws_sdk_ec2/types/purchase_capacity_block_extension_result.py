"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseCapacityBlockExtensionResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block_extension_set


class PurchaseCapacityBlockExtensionResult(TypedDict):
    capacity_block_extensions: NotRequired[
        "aws_sdk_ec2.types.capacity_block_extension_set.CapacityBlockExtensionSet"
    ]
    """<p>The purchased Capacity Block extensions. </p>"""
