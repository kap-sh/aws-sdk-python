"""Generated from Smithy shape ``com.amazonaws.ec2#ProvisionIpamPoolCidrResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool_cidr


class ProvisionIpamPoolCidrResult(TypedDict):
    ipam_pool_cidr: NotRequired["aws_sdk_ec2.types.ipam_pool_cidr.IpamPoolCidr"]
    """<p>Information about the provisioned CIDR.</p>"""
