"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam


class CreateIpamResult(TypedDict):
    ipam: NotRequired["aws_sdk_ec2.types.ipam.Ipam"]
    """<p>Information about the IPAM created.</p>"""
