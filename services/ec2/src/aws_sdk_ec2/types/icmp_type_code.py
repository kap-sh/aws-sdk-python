"""Generated from Smithy shape ``com.amazonaws.ec2#IcmpTypeCode``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer


class IcmpTypeCode(TypedDict):
    code: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The ICMP code. A value of -1 means all codes for the specified ICMP type.</p>"""
    type: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The ICMP type. A value of -1 means all types.</p>"""
