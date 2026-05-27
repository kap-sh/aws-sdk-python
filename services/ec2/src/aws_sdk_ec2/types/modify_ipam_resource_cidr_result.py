"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamResourceCidrResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_resource_cidr


class ModifyIpamResourceCidrResult(TypedDict):
    ipam_resource_cidr: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_cidr.IpamResourceCidr"
    ]
    """<p>The CIDR of the resource.</p>"""
