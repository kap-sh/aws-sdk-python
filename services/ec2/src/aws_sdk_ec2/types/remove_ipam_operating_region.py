"""Generated from Smithy shape ``com.amazonaws.ec2#RemoveIpamOperatingRegion``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class RemoveIpamOperatingRegion(TypedDict):
    region_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the operating Region you want to remove.</p>"""
