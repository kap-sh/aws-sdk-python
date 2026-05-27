"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationGroup``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CapacityReservationGroup(TypedDict):
    group_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the resource group.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the resource group.</p>"""
