"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamPoolResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool


class DeleteIpamPoolResult(TypedDict):
    ipam_pool: NotRequired["aws_sdk_ec2.types.ipam_pool.IpamPool"]
    """<p>Information about the results of the deletion.</p>"""
