"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamResourceDiscoveryResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_resource_discovery


class ModifyIpamResourceDiscoveryResult(TypedDict):
    ipam_resource_discovery: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery.IpamResourceDiscovery"
    ]
    """<p>A resource discovery.</p>"""
