"""Generated from Smithy shape ``com.amazonaws.ec2#PrivateDnsDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class PrivateDnsDetails(TypedDict):
    private_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The private DNS name assigned to the VPC endpoint service.</p>"""
