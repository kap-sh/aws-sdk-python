"""Generated from Smithy shape ``com.amazonaws.ec2#RestoreAddressToClassicResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.status
    import aws_sdk_ec2.types.string


class RestoreAddressToClassicResult(TypedDict):
    public_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Elastic IP address.</p>"""
    status: NotRequired["aws_sdk_ec2.types.status.Status"]
    """<p>The move status for the IP address.</p>"""
