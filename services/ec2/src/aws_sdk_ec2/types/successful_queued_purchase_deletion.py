"""Generated from Smithy shape ``com.amazonaws.ec2#SuccessfulQueuedPurchaseDeletion``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class SuccessfulQueuedPurchaseDeletion(TypedDict):
    reserved_instances_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Reserved Instance.</p>"""
