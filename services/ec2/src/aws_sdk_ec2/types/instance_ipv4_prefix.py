"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceIpv4Prefix``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class InstanceIpv4Prefix(TypedDict):
    ipv4_prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>One or more IPv4 prefixes assigned to the network interface.</p>"""
