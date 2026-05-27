"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class PurchaseRequest(TypedDict):
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances.</p>"""
    purchase_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The purchase token.</p>"""
