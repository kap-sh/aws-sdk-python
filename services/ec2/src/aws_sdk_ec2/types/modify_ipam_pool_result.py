"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamPoolResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool


class ModifyIpamPoolResult(TypedDict):
    ipam_pool: NotRequired["aws_sdk_ec2.types.ipam_pool.IpamPool"]
    """<p>The results of the modification.</p>"""
