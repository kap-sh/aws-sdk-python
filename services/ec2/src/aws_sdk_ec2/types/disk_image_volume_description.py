"""Generated from Smithy shape ``com.amazonaws.ec2#DiskImageVolumeDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.string


class DiskImageVolumeDescription(TypedDict):
    id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The volume identifier.</p>"""
    size: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The size of the volume, in GiB.</p>"""
