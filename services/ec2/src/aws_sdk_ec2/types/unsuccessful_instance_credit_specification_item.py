"""Generated from Smithy shape ``com.amazonaws.ec2#UnsuccessfulInstanceCreditSpecificationItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.unsuccessful_instance_credit_specification_item_error


class UnsuccessfulInstanceCreditSpecificationItem(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    error: NotRequired[
        "aws_sdk_ec2.types.unsuccessful_instance_credit_specification_item_error.UnsuccessfulInstanceCreditSpecificationItemError"
    ]
    """<p>The applicable error for the burstable performance instance whose credit option for CPU usage was not modified.</p>"""
