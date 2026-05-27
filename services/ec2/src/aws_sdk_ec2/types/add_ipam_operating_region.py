"""Generated from Smithy shape ``com.amazonaws.ec2#AddIpamOperatingRegion``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class AddIpamOperatingRegion(TypedDict):
    region_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the operating Region.</p>"""
