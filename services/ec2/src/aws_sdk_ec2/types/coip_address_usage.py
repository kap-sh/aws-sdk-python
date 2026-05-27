"""Generated from Smithy shape ``com.amazonaws.ec2#CoipAddressUsage``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CoipAddressUsage(TypedDict):
    allocation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The allocation ID of the address.</p>"""
    aws_account_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID.</p>"""
    aws_service: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services service.</p>"""
    co_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The customer-owned IP address.</p>"""
