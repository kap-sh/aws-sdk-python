"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.long


class VolumeDetail(TypedDict):
    size: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The size of the volume, in GiB.</p>"""
