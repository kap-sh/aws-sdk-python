"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesPrivateIpAddressConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class ScheduledInstancesPrivateIpAddressConfig(TypedDict):
    primary: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this is a primary IPv4 address. Otherwise, this is a secondary IPv4 address.</p>"""
    private_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address.</p>"""
